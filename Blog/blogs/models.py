from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class BlogPost(models.Model):
    """博客文章模型"""
    
    title = models.CharField(
        verbose_name="标题",
        max_length=200,
        help_text="文章标题，最多200个字符"
    )
    
    content = models.TextField(
        verbose_name="内容",
        help_text="文章正文内容"
    )
    
    owner = models.ForeignKey(
        User,
        verbose_name="作者",
        on_delete=models.CASCADE,
        related_name="blog_posts",  
        help_text="文章的作者"
    )
    
    date_added = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        editable=False  
    )
    
    last_modified = models.DateTimeField(
        verbose_name="最后修改时间",
        auto_now=True,
        help_text="文章最后修改的时间"
    )
    
    likes_count = models.PositiveIntegerField(
        verbose_name="点赞数",
        default=0,
        editable=False  
    )
    
    is_published = models.BooleanField(
        verbose_name="是否发布",
        default=True,
        help_text="控制文章是否对外可见"
    )
    
    class Meta:
        verbose_name = "博客文章"
        verbose_name_plural = "博客文章"
        ordering = ['-date_added']  
        indexes = [
            models.Index(fields=['date_added']),
            models.Index(fields=['owner', 'date_added']),
        ]
        get_latest_by = "date_added"
    
    def __str__(self):
        """返回文章标题作为字符串表示"""
        return self.title
    
    @property
    def comment_count(self):
        """获取文章的评论数量"""
        return self.comments.count()
    
    @property
    def summary(self, length=100):
        """生成文章摘要"""
        if len(self.content) <= length:
            return self.content
        return f"{self.content[:length]}..."
    
    def user_has_liked(self, user):
        """
        检查用户是否已点赞该文章
        
        Args:
            user (User): 要检查的用户对象
            
        Returns:
            bool: 用户是否已点赞
        """
        if not user or not user.is_authenticated:
            return False
        
        return self.likes.filter(user=user).exists()
    
    def increment_likes_count(self):
        """增加点赞数（原子操作）"""
        self.likes_count = models.F('likes_count') + 1
        self.save(update_fields=['likes_count'])
    
    def decrement_likes_count(self):
        """减少点赞数（原子操作）"""
        if self.likes_count > 0:
            self.likes_count = models.F('likes_count') - 1
            self.save(update_fields=['likes_count'])


class Comment(models.Model):
    """文章评论模型"""
    
    post = models.ForeignKey(
        BlogPost,
        verbose_name="关联文章",
        on_delete=models.CASCADE,
        related_name="comments",
        help_text="评论所属的文章"
    )
    
    author = models.ForeignKey(
        User,
        verbose_name="评论者",
        on_delete=models.CASCADE,
        related_name="post_comments",
        help_text="发表评论的用户"
    )
    
    content = models.TextField(
        verbose_name="评论内容",
        max_length=1000,
        help_text="评论内容，最多1000个字符"
    )
    
    created_at = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        editable=False
    )
    
    updated_at = models.DateTimeField(
        verbose_name="更新时间",
        auto_now=True,
        help_text="评论最后修改的时间"
    )
    
    is_active = models.BooleanField(
        verbose_name="是否有效",
        default=True,
        help_text="用于软删除评论"
    )
    
    parent_comment = models.ForeignKey(
        'self',
        verbose_name="父级评论",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="replies",
        help_text="如果是回复评论，则指向被回复的评论"
    )
    
    class Meta:
        verbose_name = "文章评论"
        verbose_name_plural = "文章评论"
        ordering = ['-created_at'] 
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['post', 'created_at']),
            models.Index(fields=['author', 'created_at']),
        ]
    
    def __str__(self):
        """返回评论的字符串表示"""
        return f"评论（{self.author.username} - {self.created_at.strftime('%Y-%m-%d %H:%M')}）"
    
    @property
    def short_content(self, length=50):
        """获取评论的简短内容"""
        if len(self.content) <= length:
            return self.content
        return f"{self.content[:length]}..."
    
    def is_reply(self):
        """判断是否为回复评论"""
        return self.parent_comment is not None
    
    def get_reply_count(self):
        """获取回复数量"""
        return self.replies.filter(is_active=True).count()


class Like(models.Model):
    """文章点赞模型"""
    
    post = models.ForeignKey(
        BlogPost,
        verbose_name="点赞文章",
        on_delete=models.CASCADE,
        related_name="likes",
        help_text="被点赞的文章"
    )
    
    user = models.ForeignKey(
        User,
        verbose_name="点赞用户",
        on_delete=models.CASCADE,
        related_name="post_likes",
        help_text="点赞的用户"
    )
    
    created_at = models.DateTimeField(
        verbose_name="点赞时间",
        auto_now_add=True,
        editable=False
    )
    
    class Meta:
        verbose_name = "文章点赞"
        verbose_name_plural = "文章点赞"
        ordering = ['-created_at'] 
        unique_together = ['post', 'user'] 
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['post', 'user']),
        ]
    
    def __str__(self):
        """返回点赞的字符串表示"""
        return f"{self.user.username} 点赞了《{self.post.title}》"
    
    def save(self, *args, **kwargs):
        """保存时更新文章的点赞数"""
        is_new = self.pk is None 
        super().save(*args, **kwargs)
        
        if is_new:

            self.post.increment_likes_count()
    
    def delete(self, *args, **kwargs):
        """删除时更新文章的点赞数"""
        super().delete(*args, **kwargs)
     
        self.post.decrement_likes_count()
from django.db import models


class Chat(models.Model):
    message = models.CharField(max_length=100000)
    response = models.CharField(max_length=100000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return a string representation of the Chat instance showing the id and truncated message and response."""
        return f"Chat {self.id}: {self.message[:50]} -> {self.response[:50]}"

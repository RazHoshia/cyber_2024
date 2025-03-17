import hashlib
from django.db import models
from django.utils.timezone import now

class Query(models.Model):
    hostgroup = models.IntegerField()
    schemaname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    client_address = models.GenericIPAddressField(null=True, blank=True)
    digest = models.CharField(max_length=50)
    digest_text = models.TextField()
    count_star = models.BigIntegerField()
    first_seen = models.BigIntegerField()
    last_seen = models.BigIntegerField()
    sum_time = models.BigIntegerField()
    min_time = models.BigIntegerField()
    max_time = models.BigIntegerField()
    sum_rows_affected = models.BigIntegerField()
    sum_rows_sent = models.BigIntegerField()
    created_date = models.DateTimeField(default=now, editable=False)  # Auto timestamp
    query_hash = models.CharField(max_length=64, unique=True, editable=False)  

    def compute_hash(self):
        """Compute SHA256 hash of all fields except count_star using an f-string."""
        hash_input = f"{self.hostgroup}|{self.schemaname}|{self.username}|{self.client_address}|{self.digest}|" \
                     f"{self.digest_text}|{self.first_seen}|{self.last_seen}|{self.sum_time}|{self.min_time}|" \
                     f"{self.max_time}|{self.sum_rows_affected}|{self.sum_rows_sent}|{self.created_date}"
        
        return hashlib.sha256(hash_input.encode()).hexdigest()

    def save(self, *args, **kwargs):
        if not self.query_hash:
            self.query_hash = self.compute_hash()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.created_date}: {self.schemaname} / {self.username}: {self.digest_text[:50]}..."

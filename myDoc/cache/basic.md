from django.core.cache import cache

def get_user_profile(user_id):
    cache_key = f"user_profile_{user_id}"

    # Try cache first
    profile = cache.get(cache_key)
    if profile:
        print("Cache Hit")
        return profile

    print("Cache Miss – Querying Database")
    profile = UserProfile.objects.get(id=user_id)  # Example DB query
    
    # Save in cache for next time
    cache.set(cache_key, profile, timeout=3600)  # 1 hour cache

    return profile

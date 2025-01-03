import redis

# Connect to Redis server
r = redis.Redis(host='redis.finvedic.in', port=6379, db=0, decode_responses=True)

# Setting some data in Redis for demonstration
r.set('name', 'John Doe')
r.set('age', 30)

# Reading data from Redis
name = r.get('name')
age = r.get('age')

# Print the fetched data
print(f"Name: {name}")
print(f"Age: {age}")

# If you want to retrieve all keys in the Redis database
keys = r.keys('*')
print(f"All Keys in Redis: {keys}")

# Reading data using a hash (example)
r.hset('user:1000', 'name', 'Alice')
r.hset('user:1000', 'age', 28)

# Get hash data
user_name = r.hget('user:1000', 'name')
user_age = r.hget('user:1000', 'age')

print(f"User Name: {user_name}")
print(f"User Age: {user_age}")

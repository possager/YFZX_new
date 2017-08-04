from proxy_to_redis import get_Proxy
from proxy_to_redis import redis1

for i in range(300):

    redis1.lpop('proxy_good')
#import object_class
from YouTube.YouTube_Nana.objects.object_class import User
from YouTube.YouTube_Nana.objects.post_object_class import Post

app_user_one = User("haci@gmail.com", "Zeynal", "pass", "Network Engineer")
app_user_two = User("zeynal@gmail.com", "Faraj", "pass", "Network Analyst")

app_user_one.get_user_info()
app_user_one.change_job_title("DevOps Engineer")


app_user_one.get_user_info()
app_user_two.get_user_info()
new_post = Post("This is written ", app_user_two.name)
new_post.get_post_info()

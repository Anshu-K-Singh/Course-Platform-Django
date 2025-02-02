import cloudinary
from decouple import config

SECRET_API_KEY=config('SECRET_API_KEY')

# Configuration 
# 
def cloudinary_init():      
    cloudinary.config( 
        cloud_name = "dou1efjid", 
        api_key = "215765583338978", 
        api_secret = SECRET_API_KEY, # Click 'View API Keys' above to copy your API secret
        secure=True
    )

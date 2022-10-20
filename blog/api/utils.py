import uuid
#! user uniqe id => Slug field must be uniqe

def get_random_code():
    code = str(uuid.uuid4())[:11].replace("-","")
    return code
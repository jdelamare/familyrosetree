from chalice import Chalice
from post_image_s3 import send_request

app = Chalice(app_name='familyrosetree')


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/upload_image/{image_id}', methods=['POST'], content_types=['image/png'])
def upload_image(image_id):
    
    body = app.current_request.raw_body

    object_path = '/tmp/' + image_id
    with open(object_path, 'wb') as tmp_file:
        tmp_file.write(body)

    # bucket_name = os.getenv('')
    bucket_name = ''
    object_name = image_id
    # object_path = f'/Users/n0_3nnui/Desktop/test.png'

    fields = {'Content-Type': 'png'}

    # file has 10mb max, lambda /tmp/ has 512mb max, consider upping?
    conditions = [['content-length-range', 	0, 10000000],
                ['Content-Type', 'png']]

    send_request(bucket_name, object_name, conditions, object_path=object_path)
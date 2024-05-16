import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloudresume-test')

def lambda_handler(event, context):
    try:
        response = table.get_item(Key={'id': '0'})
        item = response.get('Item')
        if item:
            views = item.get('views', 0) + 1
            print(views)
            
            response = table.put_item(Item={
                'id': '0',
                'views': views
            })
            return views
        else:
            # El elemento no existe en la tabla o no tiene la clave 'views'
            return "No se encontró el elemento o no tiene 'views'"
    except Exception as e:
        # Manejar cualquier error de DynamoDB aquí
        return str(e)

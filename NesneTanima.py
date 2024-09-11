from inference_sdk import InferenceHTTPClient

def nesne_tanima():
    from inference_sdk import InferenceHTTPClient

    CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key="LDThwaAVpbgnX16zXLwO"
    )

    result = CLIENT.infer("Market Kasa Projesi/Pictures/bootle3 - Kopya.jpeg", model_id="market_kasa_proje/1")

    class_list = [prediction['class'] for prediction in result['predictions']]
    
    return class_list
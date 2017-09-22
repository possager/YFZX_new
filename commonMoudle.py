import json
from KafkaConnector import RemoteProducer,Consumer
from saveresult import get_result_name
from sava_data_to_MongoDB import save_data_to_mongodb



def saveData(content,filename,platform_e,platform_c,news_type): #数据保存

	host = '182.150.63.40'
	port = '12308'
	username = 'silence'
	password = 'silence'
	content =json.loads(content)
	# producer = Producer(hosts=host)
	producer = RemoteProducer(host=host, port=port, username=username, password=password)
	result_file = get_result_name(plantform_e=platform_e, plantform_c=platform_c, date_time=content['data']['publish_time'],
								  urlOruid=content['data']['url'],
								  newsidOrtid=content['data']['id'],
								  datatype=news_type, full_data=content)
	# pass
	save_data_to_mongodb(data=content,item_id=result_file,platform_e=platform_e,platform_c=platform_c)
    # save_data_to_mongodb(data=content, item_id=result_file, platform_c=platform_c, platform_e=platform_e)

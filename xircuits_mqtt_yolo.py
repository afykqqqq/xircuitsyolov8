from argparse import ArgumentParser
from xai_components.base import SubGraphExecutor
from xai_components.xai_mqtt.mqtt_components import MQTTSubscribe, MQTTPublish, MQTTConnect, MQTTStartLoop
from xai_components.xai_yolov8.yolov8segmentation import Yolov8Segmentation

def main(args):
    ctx = {}
    ctx['args'] = args
    c_0 = MQTTConnect()
    c_1 = MQTTSubscribe()
    c_2 = MQTTPublish()
    c_3 = MQTTStartLoop()
    c_4 = Yolov8Segmentation()
    c_5 = MQTTPublish()
    c_0.broker.value = 'localhost'
    c_0.port.value = 1883
    c_1.topic.value = 'cvsystem/main/results'
    c_2.topic.value = 'cvsystem/main/results'
    c_2.message = c_1.message
    c_5.topic.value = 'cvsystem/main/results'
    c_0.next = c_1
    c_1.next = c_2
    c_1.on_message = SubGraphExecutor(c_4)
    c_2.next = c_3
    c_3.next = None
    c_4.next = c_5
    c_5.next = None
    next_component = c_0
    while next_component:
        (is_done, next_component) = next_component.do(ctx)
if __name__ == '__main__':
    parser = ArgumentParser()
    main(parser.parse_args())
    print('\nFinished Executing')
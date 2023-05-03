# xircuitsyolov8
 
I try to perform live video detection and link it to MQTT. However, im experiencing an issue where the MQTT loop stops when it reaches the YOLOv8 function. This is because the YOLOv8 function conducts real-time detection and continues looping until I manually stop it. im seeking advice on how to allow the MQTT to operate simultaneously with real time detection so that we can generate the output.

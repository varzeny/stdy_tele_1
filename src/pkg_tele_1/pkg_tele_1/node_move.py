import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class KeyboardSubscriber(Node):

    def __init__(self):
        super().__init__('node_move')
        self.subscription = self.create_subscription(String, 'keyboard_input', self.callback, 10)


    def callback(self, msg):
        self.get_logger().info(f'Received: "{msg.data}"')
        if msg.data == "esc":
            print("종료신호받음")
            rclpy.shutdown()
            return

def main(args=None):
    rclpy.init(args=args)
    keyboard_subscriber = KeyboardSubscriber()

    rclpy.spin(keyboard_subscriber)

    print("종료중")
    keyboard_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
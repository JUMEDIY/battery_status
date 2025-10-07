import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class BatteryPublisher(Node):
    def __init__(self):
        super().__init__('battery_publisher')
        self.publisher_ = self.create_publisher(Float32, 'battery_status', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.battery_level = 100.0

    def timer_callback(self):
        # จำลองการลดระดับแบตเตอรี่
        self.battery_level -= random.uniform(0.5, 2.0)
        if self.battery_level < 0:
            self.battery_level = 100.0

        msg = Float32()
        msg.data = self.battery_level
        self.publisher_.publish(msg)
        self.get_logger().info(f'Battery: {self.battery_level:.2f}%')

def main(args=None):
    rclpy.init(args=args)
    node = BatteryPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

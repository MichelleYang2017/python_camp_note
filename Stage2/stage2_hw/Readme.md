
## 使用说明
### 项目说明：
* 这是一个信用卡管理程序
* 用户手持信用卡购物，使用函数，按照软件开发规范
* 用户名密码存放在文件中，支持多用户登录，使用json
* 程序启动，先登录或者注册，保存信息到文件中，记录日志
* 用户的登录、密码输错3次，锁定，不能再登录
* 用户可以取现、消费、还款、提额
* 允许用户根据商品编号购买商品，用户选择商品，检测余额，够扣款，不够用提示，用户行为都要记录在日志里
* 用户可以随时退出，退出时，打印已购买商品和余额
### 目录说明
* 启动文件 start.py 存放在bin目录下
* 配置文件 settings.py 存放在conf目录下
* 核心逻辑文件 src.py 存放在 core 目录中
* 数据相关文件 db.json 存放在db目录下
* 公用方法文件 common.py 存放在lib目录下
* 日志文件 access.log 存放在log目录下
### 程序使用说明
运行之前：在运行程序之前根据包位置的不同，修改导入的包

运行：直接运行core 目录下的src.py即可
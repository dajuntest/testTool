#language: zh-CN
功能: 登录
    场景大纲: 正常登录
        假如 账号输入<account>
        而且 密码输入<password>
        而且: 输入验证码
        当: 点击 登录按钮
        那么: 登录成功

        例子: 账号数据
        | account | password |
        | 55hy04  | 1234567  |
# 專案指引

## 專案目錄結構

 - Django Templates ： 《Project》/Templates/
 - 靜態檔案： 《Project》/static/

## 建置平台

### 安裝 Bootstrap

 ```
 yarn add bootstrap
 ```

 ```
 yarn global add bootstrap
 la ~/.config/yarn/global/node_modules/bootstrap/
 ```

## 功能

### Django 用戶認證

[Django/用戶認證](https://zh.wikibooks.org/zh-tw/Django/%E7%94%A8%E6%88%B7%E8%AE%A4%E8%AF%81)

[How to change a user’s password in Django](https://canbaysal.com/2018/10/how-to-change-a-users-password-in-django/)



### 使用者管理

 - 登入： /account/login/
 - 登出： /account/logout/
 - 註冊： /account/registration/
 - 變更密碼： /account/password_change/
 - 重設密碼： /account/password_reset/

### 部落格（Blog）

## 參考

 - 程式碼來源：[《跟著老齊學 Python: Django 實戰》](https://github.com/qiwsir/DjangoPracticeProject)

 - [Django 文档内容](https://docs.djangoproject.com/zh-hans/3.2/contents/)

 - [Django中的用户认证¶](https://docs.djangoproject.com/zh-hans/3.2/topics/auth/)

 - [使用 Django 的验证系统](https://docs.djangoproject.com/zh-hans/3.2/topics/auth/default/)

 - [Part 3: Django Reset Password and Change Password](https://techpluslifestyle.com/technology/django-reset-password/)

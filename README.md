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

### 使用者管理

 - 登入： /account/login/ [name='login']
 - 登出： /account/logout/ [name='logout']
 - 註冊： /account/register/ [name='user_register']
 - 變更密碼： /account/change-password/ [name='change_password']
 - 重設密碼： /account/password-change-done/ [name='password_change_done']


### 部落格（Blog）

 - 以部落格標題，條列所有文章： / [name='blog']
 - 顯示部落格內容： /\<int:article_id>/ [name='blog_article']


## 參考

### Django 參考

 - 程式碼來源：[《跟著老齊學 Python: Django 實戰》](https://github.com/qiwsir/DjangoPracticeProject)

 - [Django V3.2 文档内容](https://docs.djangoproject.com/zh-hans/3.2/contents/)

### Django 使用者管理

__【官網文件】__

 - [Django中的用户认证¶](https://docs.djangoproject.com/zh-hans/3.2/topics/auth/)

 - [使用 Django 的验证系统](https://docs.djangoproject.com/zh-hans/3.2/topics/auth/default/)

__【分享文件】__

 - [Django/用戶認證](https://zh.wikibooks.org/zh-tw/Django/%E7%94%A8%E6%88%B7%E8%AE%A4%E8%AF%81)

 - [Part 3: Django Reset Password and Change Password](https://techpluslifestyle.com/technology/django-reset-password/)

 - [How to change a user’s password in Django](https://canbaysal.com/2018/10/how-to-change-a-users-password-in-django/)

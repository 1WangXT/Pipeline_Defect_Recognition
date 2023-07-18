# 具有涂喷以及清洗功能的无人机系统的操作手册

# **1**     引言

# 1.1   编写目的

就具有涂喷以及清洗功能的无人机系统的使用，进行说明。对它的各个模块功能，提供了示图。以便于用户使用。
------------------------------------------------------

1.2   参考资料
----------

《具有涂喷以及清洗功能的无人机系统需求分析报告》

《具有涂喷以及清洗功能的无人机系统详细设计报告》

# **2**     软件概述

2.1  软件功能
---------

（1）设备管理：对各种设备信息进行展示和操作。

（2）核心模块库管理：建立自学习核心图像模型库和模型优     化。

（3）工程任务管理：对工程配置、告警、工程站点进行管理。

（4）资料档案管理：对企业信息、项目信息、施工信息、资料     中心进行管理。

（5）突发事件管理：对事件进行监听、预警以及预案处理。

（6）运维工单管理：对异常设备进行工单的派发和报警。

（7）日志管理：记录用户调用接口日志。

## 2.2  软件运行

本系统运行在 **PC**  上，使用 **WINDOWS** 操作系统，浏览器登陆地址即可进行相应操作。

## 2.3   系统要求

**Windows XP** 以上系统，**1G** 以上内存。

# **3**     系统简要概述

通过前端智能化建设和中心管理平台的搭建，为使用者提供丰富的管理方法，为操作员提供清晰的服务。

1）         位于无人机腹部的双目摄像机自动扫描工作区，通过数据链路回传到中心平台，存储到基础数据库；

2）         利用回传的数据，系统建立工作区模型，自动规划工作航线；

3）         系统自动分配任务无人机系统，工人确认工作开始工作，启动无人机上的工作设备（喷枪）以及地面的供应泵等；

4）         无人机边工作边检测，传回工作数据，中心系统验收，记录修复点。

## 3.1   设计原则



##### 1）  统一标准

具有清洗及涂喷功能的无人机系统的建设须统一标准，系统建设在符合国家和行业相关标准及地方标准的建设要求基础上，采用先进的技术手段和标准协议，整合各类工业数据资源，在统一的标准框架下实现系统信息资源共享。

##### 2）  技术先进

采用主流的、先进的技术构建具有清洗及涂喷功能的无人机系统，实现企事业单位提出的具体需求，促进工业无人机的综合应用。

##### 3）  突出应用

具有清洗及涂喷功能的无人机系统的建设必须突出其应用，在建设中应以现实需求为导向， 以有效应用为核心，充分利用工业信息资源，结合各种应用业务，贴合动态工业大数据要求，实现对施工方式的改变提供辅助价值。

##### 4）  稳定可靠

具有清洗及涂喷功能的无人机系统的建设不是各种设备的简单组合，而是统一标准构架下的有机组成。系统采用的软硬件根据统一的规范、协议和要求选型，根据最新的标准规范，并经过具有相应资格的软件评测中心、产品检测中心的测试， 质量达标，性能稳定，能够持续有效运行，满足工业管理、监控与运营 7*24 小时不间断持续运行的需要。



### 5.4核心模型库管理

### 5.4.1图像管理

### 5.4.1.1图像管理-服务

### 5.4.1.1.1图像识别、检验

进入图像检测识别界面选择文件上传图片。

![937952d0-c4a3-4bc2-b5e2-63a523bf018b](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/937952d0-c4a3-4bc2-b5e2-63a523bf018b.png)

进行图像识别

![43cb0523-0145-482c-8834-fda641fd94f9](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/43cb0523-0145-482c-8834-fda641fd94f9.png)

结果展示

![456ce5ea-0483-48b9-b52e-628388d9a8f2](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/456ce5ea-0483-48b9-b52e-628388d9a8f2.png)

### 5.4.1.1.2图像分割

进入图像分割界面选择文件上传图片

![b5eb000b-47a2-4d78-8c41-97459f807ac0](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/b5eb000b-47a2-4d78-8c41-97459f807ac0.png)

进行图像分割

![fef19f83-a590-427d-be05-ce0a8077b988](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/fef19f83-a590-427d-be05-ce0a8077b988.png)

结果

![0bdd2d15-b2cc-45ea-863f-ec2d2c8b676e](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/0bdd2d15-b2cc-45ea-863f-ec2d2c8b676e.png)

### 5.4.1.1.3图像分类

进入图像分类界面选择文件上传图片

![483e3841-c03f-42ad-8469-5c6678756247](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/483e3841-c03f-42ad-8469-5c6678756247.png)

进入图像分类

![3a3d59ea-5bd4-4efd-bf99-5319ffaa8d8c](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/3a3d59ea-5bd4-4efd-bf99-5319ffaa8d8c.png)

结果

![99f94fd9-118d-4c1f-9cc3-985e05eba3c0](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/99f94fd9-118d-4c1f-9cc3-985e05eba3c0.png)

### 5.4.1.2图像管理-算法

**选择不同功能展示对应的算法代码**

![abdb7498-eaf1-47ef-b80b-f38548defd09](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/abdb7498-eaf1-47ef-b80b-f38548defd09.png)

![a59e7844-6998-4ffb-9a0c-bf0ff4d6af33](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/a59e7844-6998-4ffb-9a0c-bf0ff4d6af33.png)

![62f6efeb-3f16-4ba1-aaf8-7f94466ae802](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/62f6efeb-3f16-4ba1-aaf8-7f94466ae802.png)

![e729ad2a-59ce-4a6f-8594-78ce8f304bbd](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/e729ad2a-59ce-4a6f-8594-78ce8f304bbd.png)

### 5.4.1.3图像管理-详情

![0390d9fd-bb9b-4749-bdaf-5e3bc55a2db3](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/0390d9fd-bb9b-4749-bdaf-5e3bc55a2db3.png)

### 5.4.1.4图像管理-分析

![a15ee770-6c58-4e5f-aead-9da3a7f156b5](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/a15ee770-6c58-4e5f-aead-9da3a7f156b5.png)

### 5.4.2模型管理

### 5.4.2.1模型管理-详情

训练的权重（实时更新），可供下载

![90dd69bd-351a-4e51-9387-682babeaffc5](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/90dd69bd-351a-4e51-9387-682babeaffc5.png)

### 5.4.2.2模型管理-自学习

### 5.4.2.2.1数据加载

选择文件，文件格式：zip

选择文件内容：

![011251bc-1103-45f5-a7b9-92281c4faf89](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/011251bc-1103-45f5-a7b9-92281c4faf89.png)![19648a6b-980f-40d5-8031-7b71b43745cf](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/19648a6b-980f-40d5-8031-7b71b43745cf.png)![96bda5a5-c240-4db6-8147-714a19673030](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/96bda5a5-c240-4db6-8147-714a19673030.png)

![5551c5e9-f58c-487a-b403-5ca3ef816e24](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/5551c5e9-f58c-487a-b403-5ca3ef816e24.png)![1417af80-7b39-47dd-83d5-f28e6073ca3f](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/1417af80-7b39-47dd-83d5-f28e6073ca3f.png)

![0b85275a-622b-4669-9b28-6f81585de07d](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/0b85275a-622b-4669-9b28-6f81585de07d.png)

进行文件上传

![80095338-e55f-4866-a50b-02a6ee4b4435](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/80095338-e55f-4866-a50b-02a6ee4b4435.png)

![1a854398-6ecc-4952-853c-0a0a3912c9ba](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/1a854398-6ecc-4952-853c-0a0a3912c9ba.png)

![cf8bee50-5446-4171-9d0f-99149f90efb2](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/cf8bee50-5446-4171-9d0f-99149f90efb2.png)

上传成功后，点击处理文件（裁剪等预处理功能）

![0440c77b-42df-44b9-93a8-c4237c492644](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/0440c77b-42df-44b9-93a8-c4237c492644.png)

### 5.4.2.2.2数据处理

训练前，模型选择

![e3dd9433-fc1a-4074-8a0f-6b354b15325d](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/e3dd9433-fc1a-4074-8a0f-6b354b15325d.png)

开始训练

![123531fd-141c-499d-a1fd-42222dee5d92](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/123531fd-141c-499d-a1fd-42222dee5d92.png)

![3f56511b-cd7f-4e26-82c1-c688c4c2c9c4](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/3f56511b-cd7f-4e26-82c1-c688c4c2c9c4.png)

训练成功

![efc5e774-b9f2-49c3-a929-a2ed985828a2](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/efc5e774-b9f2-49c3-a929-a2ed985828a2.png)

### 5.4.2.2.3数据测试

开始验证

![a0c157cb-0fa2-434d-8e90-23ec8f01f862](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/a0c157cb-0fa2-434d-8e90-23ec8f01f862.png)

验证成功（结果显示）

![7911233c-aadf-4c09-be5b-c6e180a65f56](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/7911233c-aadf-4c09-be5b-c6e180a65f56.png)

![63ee3050-a3f2-4244-bd90-e05383575445](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/63ee3050-a3f2-4244-bd90-e05383575445.png)

### 5.4.2.2.4数据封装

开始测试

![b6b2296e-3c32-4c16-a588-04b2d504ce28](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/b6b2296e-3c32-4c16-a588-04b2d504ce28.png)

结果

![47c2cecb-7ed7-4969-9e1a-a11195d0d7be](file:///C:/Users/%E6%89%B6%E8%8B%8F/Pictures/Typedown/47c2cecb-7ed7-4969-9e1a-a11195d0d7be.png)

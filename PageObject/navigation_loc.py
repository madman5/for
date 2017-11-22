#coding:utf-8

'''
	导航栏菜单元素定位
'''
class Nav():
	nav_member_loc=("link text","成员管理")
	nav_sp1_loc=("link text","商品管理")
	nav_service_loc=("css selector","#MyAccordion > div:nth-child(3) > div.panel-header.accordion-header > div.panel-title.panel-with-icon")
	nav_shop_loc=("link text","店铺管理")
	nav_order_loc=("link text","订单管理")
	nav_school_loc=("link text","学校管理")
	nav_information_loc=("link text","信息管理")
	nav_money_loc=("link text","财务管理")
	nav_DBO_loc=("link text","运营管理")
	nav_publish_loc=("link text","出版后台")

	nav_publish_level__loc = ("link text", "管理员管理")
	nav_qx_level__loc = ("link text", "权限管理")
	nav_shanjia_level_loc = ("link text", "商家管理")
	nav_sp_level__loc = ("id", "treeadmin_id_goods") 	# 商品管理
	nav_service_level_loc = ("css selector", "#_easyui_tree_5") #服务管理
	nav_service_use_level_loc = ("link text", "服务使用情况")
	nav_present_level_loc = ("link text", "赠送服务")
	nav_wholesale_shop_level_loc = ("link text", "批发店铺管理")
	nav_shop_order_level_loc = ("link text", "微商城订单")
	nav_wholesale_order_level_loc = ("link text", "批发市场订单")
	nav_school_level_loc = ("css selector", "treeadmin_id_schoolmanager>li(1)")  #学校管理
	nav_class_level_loc = ("link text", "班级管理")
	nav_user_level_loc = ("link text", "用户管理")
	nav_send_level_loc = ("link text", "发送消息")
	nav_received_level_loc = ("link text", "已收消息")
	nav_post_level_loc = ("link text", "已发消息")
	nav_radio_level_loc = ("link text", "系统广播")
	nav_idea_level_loc = ("link text", "意见反馈")
	nav_ledger_level_loc = ("link text", "总账")
	nav_Merchants_detail_level_loc = ("link text", "商家明细")
	nav_zbjs_level_loc = ("link text", "暂不结算明细")
	nav_sjtx_level_loc = ("link text", "商家提现管理")
	nav_qdtx_level_loc = ("link text", "渠道商提现管理")
	nav_yygk_level_loc = ("link text", "运营概况")
	nav_sjtj_level_loc = ("link text", "数据统计")
	nav_tsmk_level_loc = ("link text", "听说模考")
	nav_spfm_level_loc = ("link text", "视频封面管理")
	nav_zpgl_level_loc = ("link text", "作品管理")
	nav_mlgl_level_loc = ("link text", "目录管理")
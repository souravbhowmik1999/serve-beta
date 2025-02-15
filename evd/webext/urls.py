from django.conf.urls import patterns
from django.conf.urls import url
from .views import *
from django.views.generic import TemplateView, RedirectView
from web.views import new_profile,projectsummary
# from webext.demand_views import (Demand, OnlineDemand,BookOnlineDemand,FtDemand,BookFtDemand,ContentDemand,ContentReviewCheckList,contentreview)

urlpatterns = [
    url(r'^update_offerings_date/', update_offerings_date, name='update_offerings_date'),
    url(r'^demandList/(?P<short_url>[a-zA-Z0-9-]+)?$', RedirectView.as_view(url='/demand/'), name='demandList'),
    url(r'^bulk_upload/?$', bulk_upload, name='bulk_upload'),
    url(r'^get_bulk_upload/?$', get_bulk_upload, name='get_bulk_upload'),
    url(r'^ajax/get_uploaded_data/?$', get_uploaded_data, name='get_uploaded_data'),
    url(r'^ajax/confirm_center_slot/?$', confirm_center_slot, name='confirm_center_slot'),
    url(r'^ajax/updateRoleSupport/?$', updateRoleSupport, name='updateRoleSupport'),
 
    url(r'^centerNew/?$', centerNew , name='centerNew'),
    url(r'^centers/?$', centers , name='centers'),
    url(r'^centerDetails/?$', centerDetails , name='centerDetails'),
    url(r'^ajax/time_table/?$', time_table, name='time_table'),
    url(r'^enroll_student/?$', enroll_student, name='enroll_student'),
    url(r'^save_enrollStudent/?$', save_enrollStudent, name='save_enrollStudent'),
    url(r'^enrollStudent_list/?$', enrollStudent_list, name='enrollStudent_list'),
    url(r'^getstudentLIstData/?$', getstudentLIstData, name='getstudentLIstData'),
    url(r'^edit_student/?$', edit_student, name='edit_student'),
    url(r'^delete_student/?$', delete_student, name='delete_student'),
    url(r'^ajax/get_users/?$', get_users, name='get_users'),
    url(r'^ajax/save_rating/?$', save_rating, name='save_rating'),
    url(r'^downloadTransliteration/?$', downloadSampleTransliteration, name='downloadTransliteration'),
    url(r'^downloadBulkUpload/?$', downloadSampleBulkUpload, name='downloadSampleBulkUpload'),
    url(r'^get_sesstionRating/?$',  get_sesstionRating, name=' get_sesstionRating'),
    url(r'^bulkUploadTask/?$',  upload_task, name='upload_task'),
    url(r'^testing_data/', testing_data, name='testing_data'),
    url(r'^testing_data_multi_center/', testing_data_multi_center, name='testing_data_multi_center'),
    url(r'^downloadSampleTask/?$',  downloadSampleTask, name='downloadSampleTask'),
    url(r'^task_reporting/?$', task_reporting , name='task_reporting'),
    url(r'^ajax/center_access/?$',center_access, name='center_access'),
    url(r'^ajax/get_rejected_task/?$',get_rejected_task, name='get_rejected_task'),
    url(r'^ajax/get_username/?$', get_username, name='get_username'),
    url(r'^students_log/?$',  students_log, name='students_log'),
    url(r'^get_students_log_details/?$',  get_students_log_details, name='get_students_log_details'),
    url(r'^walloffame/?$', walloffame, name='walloffame'),
    url(r'^dropTeacher/?$', dropTeacher, name='dropTeacher'),
    url(r'^demand_task/?$', demand_task, name='demand_task'),
    url(r'^ajax/save_help/?$', save_help, name='save_help'),
    url(r'^ajax/create_Task_autoAlocation/?$', create_Task_autoAlocation, name='create_Task_autoAlocation'),
    url(r'^ajax/confirm_demand/?$', ConfirmDemandView.as_view(), name='ConfirmDemandView'),
    url(r'^accept_decline_mail/?$', accept_decline_mail, name='accept_decline_mail'),
    url(r'^ajax/callMedia/?$', callMedia, name='callMedia'),
    url(r'^ajax/getCenterNameByStateType/?$', getCenterNameByStateType, name='getCenterNameByStateType'),
    url(r'^created_Session/?$', created_Session, name='created_Session'),
    url(r'^prefDaysAndPrefSlots/?$', prefDaysAndPrefSlots, name='prefDaysAndPrefSlots'),
    url(r'^custom_login/?$', custom_login, name='custom_login'),
    # url(r'^stats/?$', stats, name='stats'),
    url(r'^projectsummary/?$', projectsummary, name='projectsummary'),
    url(r'^ajax/getCentesByState/?$', getCentesByState, name='getCentesByState'),
    url(r'^ajax/getSummaryData/?$', getSummaryData, name='getSummaryData'),
    url(r'^ajax/getStatsClassesData/?$', getStatsClassesData, name='getStatsClassesData'),
    url(r'^ajax/getCenterOfferingDetails/?$', getCenterOfferingDetails, name='getCenterOfferingDetails'),
    url(r'^ajax/getCourseCoverage/?$', getCourseCoverage, name='getCourseCoverage'),
    url(r'^ajax/getAttndClassesData/?$', getAttndClassesData, name='getAttndClassesData'),
    url(r'^ajax/getSelCenters/?$', getSelCenters, name='getSelCenters'),
    url(r'^ajax/getSelUsers/?$', getSelUsers, name='getSelUsers'),
    url(r'^ajax/getCenterUsers/?$', getCenterUsers, name='getCenterUsers'),
    url(r'^ajax/getPartnerUsers/?$',  getPartnerUsers, name='getPartnerUsers'),

    url(r'^block_demand/', 'block_demand', name='block_demand'),   
    url(r'^centerNew/', centerNew , name='centerNew'),
    url(r'^centers/', centers , name='centers'),
    url(r'^centerDetails/', centerDetails , name='centerDetails'),
    url(r'^ajax/time_table/', time_table, name='time_table'),
    url(r'^enroll_student/', enroll_student, name='enroll_student'),
    url(r'^bulk_enroll_student/', bulk_enroll_student, name='bulk_enroll_student'),
    url(r'^bulk_enroll_student_multi_center/', bulk_enroll_student_multi_center, name='bulk_enroll_student_multi_center'),
    url(r'^save_enrollStudent/', save_enrollStudent, name='save_enrollStudent'),
    url(r'^enrollStudent_list/', enrollStudent_list, name='enrollStudent_list'),
    url(r'^bulk_uplaod_student_enroll/', bulk_uplaod_student_enroll, name='bulk_uplaod_student_enroll'),
    url(r'^bulk_upload_student_enroll_multi_center/', bulk_upload_student_enroll_multi_center, name='bulk_uplaod_student_enroll'),
    url(r'^getstudentLIstData/', getstudentLIstData, name='getstudentLIstData'),
    url(r'^edit_student/', edit_student, name='edit_student'),
    url(r'^delete_student/', delete_student, name='delete_student'),
    url(r'^ajax/get_users/', get_users, name='get_users'),
    url(r'^ajax/save_rating/', save_rating, name='save_rating'),
    url(r'^downloadTransliteration/', downloadSampleTransliteration, name='downloadTransliteration'),
    url(r'^downloadBulkUpload/', downloadSampleBulkUpload, name='downloadSampleBulkUpload'),
    url(r'^get_sesstionRating/',  get_sesstionRating, name=' get_sesstionRating'),
    url(r'^bulkUploadTask/',  upload_task, name='upload_task'),
    url(r'^downloadSampleTask/',  downloadSampleTask, name='downloadSampleTask'),
    url(r'^task_reporting/', task_reporting , name='task_reporting'),
    url(r'^ajax/center_access/',center_access, name='center_access'),
    url(r'^ajax/get_rejected_task/',get_rejected_task, name='get_rejected_task'),
    url(r'^ajax/get_username/', get_username, name='get_username'),
    url(r'^students_log/',  students_log, name='students_log'),
    url(r'^get_students_log_details/$',  get_students_log_details, name='get_students_log_details'),
    url(r'^walloffame/', walloffame, name='walloffame'),
    url(r'^test/?$', test, name='test'),
    url(r'^demand_task/$', demand_task, name='demand_task'),
    url(r'^ajax/save_help/', save_help, name='save_help'),
    url(r'^ajax/create_Task_autoAlocation/', create_Task_autoAlocation, name='create_Task_autoAlocation'),
    url(r'^ajax/callMedia/', callMedia, name='callMedia'),
    url(r'^ajax/getCenterNameByStateType/', getCenterNameByStateType, name='getCenterNameByStateType'),
    url(r'^created_Session/', created_Session, name='created_Session'),
    url(r'^prefDaysAndPrefSlots/', prefDaysAndPrefSlots, name='prefDaysAndPrefSlots'),
    url(r'^custom_login/', custom_login, name='custom_login'),
    # url(r'^stats/', stats, name='stats'),
    url(r'^ajax/getCentesByState/', getCentesByState, name='getCentesByState'),
    url(r'^ajax/getSummaryData/', getSummaryData, name='getSummaryData'),
    url(r'^ajax/getStatsClassesData/', getStatsClassesData, name='getStatsClassesData'),
    url(r'^ajax/getCenterOfferingDetails/', getCenterOfferingDetails, name='getCenterOfferingDetails'),
    url(r'^ajax/getCourseCoverage/', getCourseCoverage, name='getCourseCoverage'),
    url(r'^ajax/getAttndClassesData', getAttndClassesData, name='getAttndClassesData'),
    #url(r'^ajax/getSelCenters', getSelCenters, name='getSelCenters'),
    url(r'^ajax/getSelUsers', getSelUsers, name='getSelUsers'),
    url(r'^ajax/getCenterUsers', getCenterUsers, name='getCenterUsers'),
    url(r'^ajax/getCentersForPartner',getCentersForPartner,name='getCentersForPartner'),
    url(r'^stub', stub, name='stub'),
    url(r'^saveStub', saveStub, name='saveStub'),
    url(r'^ajax/get_star_childrens/?$',get_children_stars_of_month, name='get_star_childrens'),
    url(r'^ajax/get_allteachers', get_allteachers, name='get_allteachers'),
    url(r'^ajax/getSelCentersBaseOnUser/?$', getSelCentersBaseOnUser, name='getSelCentersBaseOnUser'),
    url(r'^ajax/getSchools/?$', getSchools, name='getSchools'),
    url(r'^reset_password/?$', reset_password, name='reset_password'),
    url(r'^resetpassword_done/?$', resetpassword_done, name='resetpassword_done'),
    url(r'^newevdpage/', newevdpage , name='newevdpage'),
    url(r'^my_referrals/?$', my_referrals, name='my_referrals'),
    url(r'^ajax/my_referrals_details/', my_referrals_details, name='my_referrals_details'),
    url(r'^plan_topics/(?P<cent_id>\d+)/(?P<off_id>\d+)/?$', plan_topics, name='plan_topics'),
    url(r'^change_grade/?$', change_grade, name='change_grade'),
    url(r'^get_sub_topic/?$', get_sub_topic, name='get_sub_topic'),
    url(r'^modify_topics/?$', modify_topics, name='modify_topics'),
    url(r'^delete_duplicate_data/?$', delete_duplicate_data, name='delete_duplicate_data'),
    url(r'^change_password/?$', change_password,name='change_password'),
    #url(r'^new_home/?$',TemplateView.as_view(template_name='new_ui_home.html'),name="homepage"),
    url(r'^class_completion_dashboard/?$', TemplateView.as_view(template_name='class_completion_dashboard.html'), name='class_completion_dashboard'),
    url(r'^teacher_dashboard/?$', TemplateView.as_view(template_name='teacher_dashboard.html'), name='teacher_dashboard'),
    url(r'^offering_dashboard/?$', TemplateView.as_view(template_name='offering_dashboard.html'), name='offering_dashboard'),
    url(r'^partner_dashboard/?$', TemplateView.as_view(template_name='partner_dashboard.html'), name='partner_dashboard'),
    url(r'^reports/?$', reports, name="reports"),
    url(r'^report_load/?$',  report_load, name=" report_load"),
    url(r'^new_start_page/?$', TemplateView.as_view(template_name='new_start_page.html'), name="new_start_page"),
    url(r'^vLounge/?$', new_landing_view, name="new_landing_page"),
    url(r'^opportunity_page/?$', TemplateView.as_view(template_name='opportunity_page.html'), name="opportunity_page"),
    url(r'^next_opportunity_page/?$', TemplateView.as_view(template_name='next_opportunity_page.html'), name="next_opportunity_page"),
    url(r'^slot_page/?$', TemplateView.as_view(template_name='slot_page.html'),name="slot_page"),
    url(r'^gallery/?$', TemplateView.as_view(template_name='gallery.html'),name="gallery"),
    url(r'^final_page/?$', TemplateView.as_view(template_name='final_page.html'), name="final_page"),
    url(r'^new_signup', new_signup, name='new_signup'),
    url(r'^vol_of_fame/?$', vol_of_fame, name="vol_of_fame"),
    url(r'^update-centerInfo/?$',update_centerInfo, name="update_centerInfo"),
    url(r'^showMap/?$',show_map, name="show_map"),
    url(r'^getDifferentDate/?$',get_differentDate, name="get_differentDate"),
    url(r'^cancelled-sesssion-status/?$',cancelled_sesssion_status, name="cancelled_sesssion_status"),
    url(r'^tsd_details/?$',tsd_details, name="tsd_details"),
    url(r'^tsd_user_details//?$',tsd_user_details, name="tsd_user_details"),
    url(r'^update_no_profile/?$',add_userprofile),
    url(r'^save_rubaru_even_data/?$',save_rubaru_even_data,name='save_rubaru_even_data'),
    url(r'^ajax/getExternalRoleVolunteer/?$',get_external_roles_volunteer),
    url(r'^ajax/getExternalRolePartner/?$',get_external_roles_partner),
    url(r'^ajax/getExternalRolepam/?$',get_external_roles_pam),
    url(r'^confirm_pam/?$',confirm_pam),
    url(r'^get_student_db/?$',get_student_db),
    url(r'^role/?$', authenticated_user_role,name="authenticated_user_role"),
    url(r'^role_funding/?$', authenticated_funding_role,name="authenticated_funding_role"),
    url(r'^remove_pam/?$',remove_pam),
    url(r'^remove_offering/?$',remove_offering),
    url(r'^ajax/getStickerAndReason/?$',get_sticker_and_reason),
    url(r'^ajax/getPam/?$',getPam),
    url(r'^ajax/submittAppreciation/?$',submitt_appreciation),
    url(r'^add_vol_of_month/?$',add_vol_of_month, name="add_vol_of_month"),
    url(r'^ajax/get_vol_of_month/?$',get_vol_of_month, name="get_vol_of_month"),
    url(r'^ajax/save_vol_of_month/?$',save_vol_of_month, name="save_vol_of_month"),
    url(r'^list_vol_of_month/?$',list_vol_of_month, name="list_vol_of_month"),
    url(r'^edit_vol_of_month/?$',edit_vol_of_month, name="edit_vol_of_month"),
    url(r'^holidaylist/?$', holidaylistform, name="holidaylistform"),
    url(r'^updateHoliday/?$', updateHoliday, name="updateHoliday"),
    url(r'^deleteHoliday/?$', deleteHoliday, name="deleteHoliday"),
    url(r'^addholiday/?$', AddHolidays, name="AddHolidays"),
    url(r'^Applyholidays/?$', Apply_holidays, name="Applyholidays"),
    url(r'^getboards/?$', getboards, name="getboards"),
    url(r'^Delete_singleoffering_Sessions/?$', Delete_singleoffering_Sessions, name="Delete_singleoffering_Sessions"),
    url(r'^fetch_apply_holiday/?$',fetch_apply_holiday,name="fetch_apply_holiday"),
    url(r'^get_holidaysList_to_add_holiday/?$',get_holidaysList_to_add_holiday,name="get_holidaysList_to_add_holiday"),
    url(r'^get_academic_years_by_board/?$',get_academic_years_by_board,name="get_academic_years_by_board"),
    url(r'^get_calender_by_academic_id/?$',get_calender_by_academic_id,name="get_calender_by_academic_id"),
    url(r'^get_country_state_city/?$', get_country_state_city, name='get_country_state_city'),
    url(r'^provisional_demand/?$', provisional_demand, name="provisional_demand"),
    url(r'^add_provisional_demand/', add_provisional_demand, name="add_provisional_demand"),
    url(r'^update_provisional_demand/', update_provisional_demand, name="update_provisional_demand"),
    url(r'^delete_provisional_demand/', delete_provisional_demand, name="delete_provisional_demand"),
    url(r'^drop_provisional_booking/', drop_provisional_demand_slot, name="drop_provisional_booking"),
    url(r'^provisional_volunteers_list/', provisionally_booked_demands, name='provisional_volunteers_list'),
    url(r'^get_slot_time/?$', get_provisional_center_time, name='get_slot_time'),
    url(r'^get_session_url/', get_session_url,name = 'get_session_url'),
    url(r'^verify_teacher/', verify_teacher, name='verify_teacher'),
    url(r'^verify_teacher_csd_tsd/', verify_teacher_csd_tsd, name='verify_teacher_csd_tsd'),
    url(r'^thank_you/?$', donation_give_india, name='thank_you'),
    url(r'^topic_name/', topic_name, name='topic_name'),

    url(r'^std_deleting_student/?$', deleting_student,name="std_deleting_student"),
    url(r'^students_grade_promotion/?$', students_grade_promotion,name="students_grade_promotion"),
    url(r'^get_centers_by_district/?$', get_centers_by_district,name="get_centers_by_district"),
    url(r'^update_scholastic_lfh/?$', update_scholastic_lfh, name='update_scholastic_lfh'),
    url(r'^add_lfh_scholastics/?$', add_lfh_scholastics, name='add_lfh_scholastics'),
    url(r'^sign_up_school_admin/?$', school_admin_signup, name='school_admin_signup'),
    url(r'^school_admin/users/?$', school_admin_users, name='school_admin_users'),
    url(r'^schooladmin/save_user/?$', school_admin_teachers_signup, name='save_user'),
    url(r'^schooladmin/update_school/?$', update_school, name='update_school'),
    url(r'^myschools/?$', list_schooladmin_schools, name='myschools'),
    url(r'^myschool/(?P<myschool_id>\d+)?/?$', view_schooladmin_myschool, name='view_myschool'),
    url(r'^get_videos/?$', get_videos, name='get_videos'),
    url(r'^update_video/session/?$', update_video_for_session, name='update_video_for_session'),
    url(r'^school_admins/(?P<schooladmin_id>\d+)?/?$', list_schooladmin, name='list_schooladmin'),
    url(r'^update_schooladmin_status/(?P<schooladmin_id>\d+)?/?$', update_schooladmin_status, name='update_schooladmin_status'),
	# url(r'^schooladmin/schools/(?P<school_id>\d+)?/?$', list_schooladmin_myschools, name='list_schooladmin_schools'),
    url(r'^video/tool/?$', video_tool, name='video_tool'),
    url(r'^update/pledge_details/?$', update_pledge_details, name='update_pledge_details'),
    url(r'^delete/pledge_details/?$', delete_pledge_details, name='delete_pledge_details'),
    url(r'^edit/pledge_details/?$', edit_pledge, name='edit_pledge'),
    url(r'^new_year/?$', TemplateView.as_view(template_name='new_year.html'), name='new_year'),
    url(r'^sponsor/thankyou/?$', TemplateView.as_view(template_name='donation_response_fail.html'),name='donation_response_fail'),
    url(r'^2021_Newsletter/?$', TemplateView.as_view(template_name='newsletter_2021.html'), name='Newsletter'),
    url(r'^quiz_result/?$', QuizResult.as_view(), name='quiz_result'),
    url(r'^quiz_filter/?$', quizfilter, name='quizfilter'),
    url(r'^center/subject/studentdoubts?$', student_doubt_list, name='student_doubt_list'),
    url(r'^center/doubt/detail?$', student_doubt_detail, name='student_doubt_detail'),
    url(r'^center/doubt/respond?$', student_doubt_respond, name='student_doubt_respond'),
    url(r'^center/doubt/responseedit?$', student_edit_doubt_respond, name='student_edit_doubt_respond'),
    url(r'^center/topics/?$', TopicDetailsView.as_view(), name='topic_details_by_center'),
    url(r'^center/sub-topics/?$', SubTopicDetailsView.as_view(), name='sub_topic_details_by_center'),
    url(r'^offering/topic-details/?$', TopicDetailsView.as_view(), name="TopicDetailsView"),
    url(r'^subtopic/content-details/?$', SubTopicDetailsView.as_view(), name="SubTopicDetailsView"),
    url(r'^student-reach-status/?$', student_reach_status, name='student_reach_status'),
    url(r'^flm-attendance/?$', FlmStudentAttendanceView.as_view(), name="FlmStudentAttendanceView"),
    url(r'^check-kyc-number/', check_kyc_number, name='check_kyc_number'),
    url(r'^bulk-promote-students/', BulkPromoteStudents.as_view(), name='bulk_promote_students'),
    url(r'^flm-content-view-status/', FlmContentStatusView.as_view(), name='FlmContentStatusView'),
    url(r'^sql-editor/', SqlView.as_view(), name='SqlView'),
    # demand api's
    url(r'^demand/?$', Demand.as_view(), name='DemandView'),
    url(r'^demand/gatewaysearch?$', beckn_bgsearch, name='beckn_bgsearch'),
    url(r'^demand/postvolsearch?$', beckn_postvol, name='beckn_postvol'),
    url(r'^demand/search?$', beckn_volsearch2, name='beckn_volsearch2'),
    url(r'^volunteer/searchneed?$', beckn_view, name='beckn_view'),
    url(r'^demand/on_search?$', beckn_bap_onsearch, name='beckn_bap_onsearch'),
    url(r'^demand/searchvolunteer?$', beckn_volsearch, name='beckn_volsearch'),
    url(r'^volunteer/search?$', beckn_search, name='beckn_search'),
    url(r'^demand/dsepsearch?$', beckn_dsepsearch, name='beckn_dsepsearch'),
    url(r'^demand/select?$', beckn_select, name='beckn_select'),
    url(r'^demand/bppcall?$', beckn_searchbg, name='beckn_searchbg'),
    url(r'^demand/online/?$', OnlineDemand.as_view(), name='OnlineDemandView'),
    url(r'^demand/online/book/?$', BookOnlineDemand.as_view(), name='OnlineDemandView'),
    url(r'^demand/ft/?$', FtDemand.as_view(), name='FtDemandView'),
    url(r'^demand/ft/book/?$', BookFtDemand.as_view(), name='BookFtDemandView'),
    url(r'^demand/content/?$', ContentDemand.as_view(), name='ContentDemandView'),
    url(r'^demand/otherskill/?$', OtherSkill.as_view(), name='OtherSkill'),
    url(r'^demandListForOtherSkills', demandListForOtherSkills, name='demandListForOtherSkills'),
    url(r'^demand/stats/?$', StatsDemand.as_view(), name='OfferingReport'),    
    url(r'^content_review_check_list/?$', ContentReviewCheckList.as_view(), name='ContentReviewCheckListView'),
    url(r'^search-teacher/?$', search_teacher, name='search_teacher'),
    url(r'^assistance/?$', Assistance.as_view(), name='Assistance'),
    
    
    url(r'^book-slots/?$', BookSlots.as_view(), name='BookSlotsView'),   
    url(r"^publish_booking_slots/?$", PublishBookingSlots.as_view(), name="PublishBookingSlots"), 
    url(r"^activities/?$", ActivitySystem.as_view(), name="ActivitySystem"),
    url(r"^activity_types/?$", ActivityTypes.as_view(), name="ActivityTypes"),   
 
    url(r'^flm-doubts/', FlmDoubtsThread.as_view(), name='FlmDoubtsThread'),
    url(r'^admin/content/upload/', ContentUploadView.as_view(), name='ContentUploadView'),
    url(r'^get-similar-course/', SimilarCourse.as_view(), name='SimilarCourse'),
    # This url mapping has to be the last one here.. any new one please add above
    url(r'^(?P<type_name>\w+)?/?$', getHolidaysDropdowns,name="getHolidaysDropdowns"),
    ]

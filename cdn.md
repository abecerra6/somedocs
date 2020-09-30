# CDN content in Webapp

## DB tables

Some entries are inserted by:
old? https://github.com/6connexsource/webapp/blob/master/misc/scripts/db/archived_scripts/server_environment.sql 
https://github.com/6connexsource/webapp/blob/master/misc/scripts/db/6connex_db_initialization_server_environment.sql


| Table              | Class |
| ----               | ----- |
|cdn                | Cdn |
|client_cdn         | CdnClient |
|vep_cdn            | VirtualExperienceCdn |
|server_environment | |

```
cdn
id	vendor	url	support_ssl
1	Local CDN	https://demo.6connexlocal.com/upload/	1
2	Local CDN (Secure)	https://demo.6connexlocal.com/upload/	1
client_cdn
id	client_id	cdn_id	use_directory	use_percentage	is_default	priority
1	2	2		100	1	1
2	3	1		100	1	1
vep_cdn
id	virtual_experience_id	cdn_id	use_directory	use_percentage	is_default	priority
1	1	2		100	1	1
2	2	2		100	1	1
server_environment
id, name, value
'4', 'sa.fileupload.path', '/opt/nfs/upload/'
'5', 'ca.fileupload.path', '/opt/nfs/upload/'
'6', 'cp.fileupload.path', '/opt/nfs/upload/'
'7', 'po.fileupload.path', '/opt/nfs/upload/'
'8', 'ws.fileupload.path', '/opt/nfs/upload/'
```

## Upload methods 

```
FileUploadUtil.uploadFiles(fileItems, isTemp, uploadPath, rootFilePath)
FileUploadUtil.upLoadFilesWithName(fileItems, isTemp, uploadPath, rootFilePath, String fileName)
```

Defined in:
https://github.com/6connexsource/webapp/blob/959de73ed4d185bc02bc111c27b1248062443f7f/core/src/main/java/com/sixconnex/core/util/FileUploadUtil.java#L124
https://github.com/6connexsource/webapp/blob/959de73ed4d185bc02bc111c27b1248062443f7f/core/src/main/java/com/sixconnex/core/util/FileUploadUtil.java#L175


## Upload path

Private method `FileUploadUtil.getCurrentFileUploadPath` defined in:
https://github.com/6connexsource/webapp/blob/959de73ed4d185bc02bc111c27b1248062443f7f/core/src/main/java/com/sixconnex/core/util/FileUploadUtil.java#L434

is called by `get{CA,CP}CurrentFileUploadPath` and joins (given) path with /userTargetId/targetExperienceId
e.g /upload/2/1

Some controllers use a SecureFileUploadPath if the event is secured.

| Call                                                         | uploadPath                          | rootFilePath           |
| -----------                                                  | -----------                         | ------------           |
|     clientadmin                                                                                                             |
| GeneralSettingsController.saveGeneralSettings                | getCACurrentFileUploadPath          | getCAFileUploadPath    |
| LibraryController.addContent                                 | getCACurrentFileUploadPath          | getCAFileUploadPath    |
| LibraryController.editContent                                | getCACurrentFileUploadPath          | getCAFileUploadPath    |
| TemplatesAPIController.uploadFile                            | getCACurrentFileUploadPath          | getCAFileUploadPath    |
|     controlpanel                                                                                                            |
| ContentLibrariesController.cloneContent                      | getCPCurrentSecuredFileUploadPath   | getCPFileUploadPath    | 
|                                                              | or getCPCurrentFileUploadPath       |                        |
| ContentLibrariesController.addContent                        | getCPCurrentSecuredFileUploadPath   | getCPFileUploadPath    |
|                                                              | or getCPCurrentFileUploadPath       |                        |
| ContentLibrariesController.editContent                       | getCPCurrentSecuredFileUploadPath   | getCPFileUploadPath    |
|                                                              | or getCPCurrentFileUploadPath       |                        |
| EmailMarketingController.addEmail                            | getCPCurrentFileUploadPath          | getCPFileUploadPath    |
| EmailMarketingController.updateEmailMarketing                | getCPCurrentFileUploadPath          | getCPFileUploadPath    |
| FileFetcherController.uploadFile                             | getCPCurrentFileUploadPath          | getCPFileUploadPath    |
| FilesAPIController.uploadFile                                | getCPCurrentFileUploadPath          | getCPFileUploadPath    |
| GeneralSettingController.setCustomizeNavigation              | getCPCurrentFileUploadPath          | getCPFileUploadPath    |                                      | GeneralSettingController.redirectVEConfig                    | getCPCurrentFileUploadPath          | getCPFileUploadPath    |
| GeneralSettingController.uploadicon                          | getCPCurrentFileUploadPath          | getCPFileUploadPath    |
| GeneralSettingController.setVEConfig                         | getCPCurrentFileUploadPath          | getCPFileUploadPath    |
| ManageLoginController.getVirtualExperienceConfig             | getCPCurrentFileUploadPath          | getCPFileUploadPath    |
| ManageRegistrationController.editWebinarRegistrationSetting  | getCPCurrentFileUploadPath          | getCPFileUploadPath    |
| ManageThankYouController.getVirtualExperienceConfig          | getCPCurrentFileUploadPath          | getCPFileUploadPath    |
| VirtualSpaceController.uploadFile                            | getCPCurrentSecuredFileUploadPath   | getCPFileUploadPath    |
|                                                              | or getCPCurrentFileUploadPath       |                        |
|     virtualbuilder.controller                                                                                               |
| FileController.upload                                        | getCPCurrentFileUploadPath          | getCPFileUploadPath    |
| FileController.uploadImage                                   | getCPCurrentFileUploadPath          | getCPFileUploadPath    |
| FileController.compressionImage                              | getCPCurrentFileUploadPath          | getCPFileUploadPath    |


## Other classes related to CDN content

`CDNProtectionFilter.doFilter`, in:
https://github.com/6connexsource/webapp/blob/959de73ed4d185bc02bc111c27b1248062443f7f/upload/src/main/java/com/sixconnex/files/CDNProtectionFilter.java#L57

calls `CDNResourceFinder.sendResource`, which calls `feedContent`
https://github.com/6connexsource/webapp/blob/959de73ed4d185bc02bc111c27b1248062443f7f/upload/src/main/java/com/sixconnex/files/CDNResourceFinder.java#L66

to send file as mime content

`CDNProtector.checkAccessibility` checks if cookie SA(secure akamai) is present and not expired

`AccessPathValidator.isAuthorized` checks the if the cookie has inside a path to allow access

`ReceivedAkamaiCookie` cookie format

  ip=58.240.172.196~expires=1297763110~access=/secured/4/310/*~md5=97fb68f9de180a1f29fecc3aa240ad25

## S3 content upload

`S3Uploader.upload`, defined in:
https://github.com/6connexsource/webapp/blob/9fd1f46f81997642309e09dc778f12cf66941a70/dw/src/main/java/com/sixconnex/dw/batchexport/S3Uploader.java#L26

is used in:
https://github.com/6connexsource/webapp/blob/9fd1f46f81997642309e09dc778f12cf66941a70/reports/src/main/java/com/sixconnex/reports/batchexport/service/impl/BatchExportTaskServiceImpl.java#L51



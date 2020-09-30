# CDN content

- Understand CDN code in event
  when content is accessed
- In webapp: when webapp is uploaded (low priority)
table content attr path (known)
how upload folder is choosen

Webapp
table 		class
cdn		Cdn
client_cdn	CdnClient
vep_cdn		VirtualExperienceCdn


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

CDNProtectionFilter.doFilter
 calls CDNResourceFinder.sendResource -> feedContent 
  send file as mime content


CDNProtector.checkAccessibility checks if cookie SA(secure akamai) is present and not expired

AccessPathValidator.isAuthorized 
checks the if the cookie has inside a path to allow access

ReceivedAkamaiCookie
  format
  ip=58.240.172.196~expires=1297763110~access=/secured/4/310/*~md5=97fb68f9de180a1f29fecc3aa240ad25


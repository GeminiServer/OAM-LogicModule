import sys
Import("env")
config = env.GetProjectConfig()

platform_pkg_os = "platform_packages_win32"
if sys.platform == "win32":
    platform_pkg_os = config.get("common_rp2040", "platform_packages_win32")
elif sys.platform == "linux2":
    platform_pkg_os = config.get("common_rp2040", "platform_packages_linux")
elif sys.platform == "darwin":
    platform_pkg_os = config.get("common_rp2040", "platform_packages_macos")

print("OS system is : ",sys.platform)
#print(env.Dump())

platform_pkg_common = config.get("common_rp2040", "platform_packages")
platform_pkg_new = platform_pkg_common + platform_pkg_os
config.set("common_rp2040", "platform_packages", platform_pkg_new )
print("Using platform_packages:")
current_platform_packages = config.get("common_rp2040", "platform_packages")
print(current_platform_packages)
print("Done.")
print("")


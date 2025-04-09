[app]
title = eBook Social Share
package.name = ebookshare
package.domain = org.sarkahn
source.dir = .
source.include_exts = py,kv,md
version = 0.1
requirements = python3,kivy,kivymd
orientation = portrait
fullscreen = 1
icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 33
android.minapi = 21
android.ndk = 23b
android.sdk = 24
android.ndk_path = 
android.sdk_path = 
android.private_storage = True

# Optional: boost compatibility
android.enable_androidx = True
android.use_android_native_api = False

[output]
# You’ll get an APK in ./bin/

# Note: Replace `icon.png` with your own app icon.
# 512x512 PNG works best.

plugins {
    id("com.android.application")
}

android {
    namespace = "com.yueshu.clinic"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.yueshu.clinic"
        minSdk = 24
        targetSdk = 34
        versionCode = 2
        versionName = "1.0.1"
    }

    signingConfigs {
        getByName("debug") {
            System.getenv("DEBUG_KEYSTORE_FILE")?.let { keystorePath ->
                storeFile = file(keystorePath)
                storePassword = "android"
                keyAlias = "androiddebugkey"
                keyPassword = "android"
            }
        }
    }

    buildTypes {
        release {
            isMinifyEnabled = false
        }
    }
}

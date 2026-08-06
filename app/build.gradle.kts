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

    buildTypes {
        release {
            isMinifyEnabled = false
        }
    }
}

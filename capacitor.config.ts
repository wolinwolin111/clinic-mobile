import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.clinic.rehab',
  appName: '悦舒康复',
  webDir: 'www',
  server: {
    // 手机端直接访问 VPS，不使用本地 server
    cleartext: true  // 允许 HTTP 请求
  },
  android: {
    allowMixedContent: true
  }
};

export default config;

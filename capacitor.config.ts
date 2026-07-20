import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.clinic.rehab',
  appName: '悦舒康复',
  webDir: 'www',
  server: {
    url: 'http://66.154.101.204/mobile/',
    cleartext: true
  },
  android: {
    allowMixedContent: true
  }
};

export default config;

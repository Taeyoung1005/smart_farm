# HC-06 블루투스 모듈
// 블루투스 모드 진입

sudo bluetoothctl

// 블루투스 스캔

scan on

default-agent

// 블루투스 연결

pair 블루투스주소

// 블루투스 스캔 종료

scan off

//블루투스 모듈 시리얼포드 열기 및 연결

sudo rfcomm connect hci0 주소

---

아두이노 무선업로드 시 아두이노 전원 버튼 눌러주기

그 후 시리얼통신

---
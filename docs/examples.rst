Examples
========

Basic Use
---------

A basic run looks like this::

   [tykling@container1 ~]$ sudo mobile_modem_exporter /var/tmp/node_exporter/mobile_modem.prom /dev/modem-quectel-control /dev/modem-huawei-control 
   2020-11-06 12:02:10 +0000 INFO mobile_modem_exporter Initialising serial ports...
   2020-11-06 12:02:12 +0000 INFO mobile_modem_exporter Initialising serial ports...
   2020-11-06 12:02:14 +0000 INFO mobile_modem_exporter Entering main loop, writing metrics for modems ['/dev/modem-quectel-control', '/dev/modem-huawei-control'] to /var/tmp/node_exporter/mobile_modem.prom, sleeping 10 seconds between runs...
   ^CTraceback (most recent call last):
     File "mobile_modem_exporter.py", line 312, in <module>
       init()
     File "mobile_modem_exporter.py", line 308, in init
       main()
     File "mobile_modem_exporter.py", line 234, in main
       time.sleep(args.sleep)
   KeyboardInterrupt
   [tykling@container1 ~]$ 

Debug Mode
----------

The same thing with debug mode enabled::

   [tykling@container1 ~]$ sudo mobile_modem_exporter --debug /var/tmp/node_exporter/mobile_modem.prom /dev/modem-quectel-control /dev/modem-huawei-control 
   2020-11-06 12:05:14 +0000 DEBUG mobile_modem_exporter.main():140:  Initialising serial ports and Prometheus objects...
   2020-11-06 12:05:14 +0000 INFO mobile_modem_exporter.main():186:  Initialising serial ports...
   2020-11-06 12:05:14 +0000 DEBUG mobile_modem_exporter.main():187:  Opening serial port /dev/modem-quectel-control and getting modem info...
   2020-11-06 12:05:14 +0000 DEBUG mobile_modem_exporter.__init__():54:  Configuring serial port /dev/modem-quectel-control ...
   2020-11-06 12:05:14 +0000 DEBUG mobile_modem_exporter.open():75:  Opening serial port...
   2020-11-06 12:05:14 +0000 DEBUG mobile_modem_exporter.open():82:  Serial port opened OK!
   2020-11-06 12:05:14 +0000 DEBUG mobile_modem_exporter.run():107:  Sending payload line: ATI
   2020-11-06 12:05:15 +0000 DEBUG mobile_modem_exporter.run():114:  Collecting output, looking for one of these regular expressions: ['OK']
   2020-11-06 12:05:15 +0000 DEBUG mobile_modem_exporter.run():116:  Will stop collecting after 1 matches
   2020-11-06 12:05:15 +0000 DEBUG mobile_modem_exporter.run():120:  Found match: 'OK' (match number 1 of 1)
   2020-11-06 12:05:15 +0000 DEBUG mobile_modem_exporter.run():127:  Done! Returning 53 bytes of output from serial device
   2020-11-06 12:05:15 +0000 DEBUG mobile_modem_exporter.run():107:  Sending payload line: AT+GSN
   2020-11-06 12:05:16 +0000 DEBUG mobile_modem_exporter.run():114:  Collecting output, looking for one of these regular expressions: ['OK']
   2020-11-06 12:05:16 +0000 DEBUG mobile_modem_exporter.run():116:  Will stop collecting after 1 matches
   2020-11-06 12:05:16 +0000 DEBUG mobile_modem_exporter.run():120:  Found match: 'OK' (match number 1 of 1)
   2020-11-06 12:05:16 +0000 DEBUG mobile_modem_exporter.run():127:  Done! Returning 32 bytes of output from serial device
   2020-11-06 12:05:16 +0000 INFO mobile_modem_exporter.main():186:  Initialising serial ports...
   2020-11-06 12:05:16 +0000 DEBUG mobile_modem_exporter.main():187:  Opening serial port /dev/modem-huawei-control and getting modem info...
   2020-11-06 12:05:16 +0000 DEBUG mobile_modem_exporter.__init__():54:  Configuring serial port /dev/modem-huawei-control ...
   2020-11-06 12:05:16 +0000 DEBUG mobile_modem_exporter.open():75:  Opening serial port...
   2020-11-06 12:05:16 +0000 DEBUG mobile_modem_exporter.open():82:  Serial port opened OK!
   2020-11-06 12:05:16 +0000 DEBUG mobile_modem_exporter.run():107:  Sending payload line: ATI
   2020-11-06 12:05:17 +0000 DEBUG mobile_modem_exporter.run():114:  Collecting output, looking for one of these regular expressions: ['OK']
   2020-11-06 12:05:17 +0000 DEBUG mobile_modem_exporter.run():116:  Will stop collecting after 1 matches
   2020-11-06 12:05:17 +0000 DEBUG mobile_modem_exporter.run():120:  Found match: 'OK' (match number 1 of 1)
   2020-11-06 12:05:17 +0000 DEBUG mobile_modem_exporter.run():127:  Done! Returning 146 bytes of output from serial device
   2020-11-06 12:05:17 +0000 DEBUG mobile_modem_exporter.run():107:  Sending payload line: AT+GSN
   2020-11-06 12:05:18 +0000 DEBUG mobile_modem_exporter.run():114:  Collecting output, looking for one of these regular expressions: ['OK']
   2020-11-06 12:05:18 +0000 DEBUG mobile_modem_exporter.run():116:  Will stop collecting after 1 matches
   2020-11-06 12:05:18 +0000 DEBUG mobile_modem_exporter.run():120:  Found match: 'OK' (match number 1 of 1)
   2020-11-06 12:05:18 +0000 DEBUG mobile_modem_exporter.run():127:  Done! Returning 32 bytes of output from serial device
   2020-11-06 12:05:18 +0000 INFO mobile_modem_exporter.main():212:  Entering main loop, writing metrics for modems ['/dev/modem-quectel-control', '/dev/modem-huawei-control'] to /var/tmp/node_exporter/mobile_modem.prom, sleeping 10 seconds between runs...
   2020-11-06 12:05:18 +0000 DEBUG mobile_modem_exporter.main():218:  Getting CSQ from device: /dev/modem-quectel-control
   2020-11-06 12:05:18 +0000 DEBUG mobile_modem_exporter.run():107:  Sending payload line: AT+CSQ
   2020-11-06 12:05:19 +0000 DEBUG mobile_modem_exporter.run():114:  Collecting output, looking for one of these regular expressions: ['OK']
   2020-11-06 12:05:19 +0000 DEBUG mobile_modem_exporter.run():116:  Will stop collecting after 1 matches
   2020-11-06 12:05:19 +0000 DEBUG mobile_modem_exporter.run():120:  Found match: 'OK' (match number 1 of 1)
   2020-11-06 12:05:19 +0000 DEBUG mobile_modem_exporter.run():127:  Done! Returning 28 bytes of output from serial device
   2020-11-06 12:05:19 +0000 DEBUG mobile_modem_exporter.main():227:  parsed AT+CSQ output to rssi 31 and BER 99
   2020-11-06 12:05:19 +0000 DEBUG mobile_modem_exporter.main():218:  Getting CSQ from device: /dev/modem-huawei-control
   2020-11-06 12:05:19 +0000 DEBUG mobile_modem_exporter.run():107:  Sending payload line: AT+CSQ
   2020-11-06 12:05:20 +0000 DEBUG mobile_modem_exporter.run():114:  Collecting output, looking for one of these regular expressions: ['OK']
   2020-11-06 12:05:20 +0000 DEBUG mobile_modem_exporter.run():116:  Will stop collecting after 1 matches
   2020-11-06 12:05:20 +0000 DEBUG mobile_modem_exporter.run():120:  Found match: 'OK' (match number 1 of 1)
   2020-11-06 12:05:20 +0000 DEBUG mobile_modem_exporter.run():127:  Done! Returning 28 bytes of output from serial device
   2020-11-06 12:05:20 +0000 DEBUG mobile_modem_exporter.main():227:  parsed AT+CSQ output to rssi 21 and BER 99
   2020-11-06 12:05:20 +0000 DEBUG mobile_modem_exporter.main():233:  Sleeping 10 seconds before next run...
   ^CTraceback (most recent call last):
     File "mobile_modem_exporter.py", line 312, in <module>
       init()
     File "mobile_modem_exporter.py", line 308, in init
       main()
     File "mobile_modem_exporter.py", line 234, in main
       time.sleep(args.sleep)
   KeyboardInterrupt
   [tykling@container1 ~]$ 


Metrics
-------

An example of the metrics exported for two modems::

   [tykling@container1 ~]$ cat /var/tmp/node_exporter/mobile_modem.prom 
   # HELP mobile_modem_up This metric is always 1 if the mobile_modem scrape worked, 0 if there was a problem getting info from one or more modems.
   # TYPE mobile_modem_up gauge
   mobile_modem_up 1.0
   # HELP mobile_modem_build_info Information about the mobile_modem_exporter itself.
   # TYPE mobile_modem_build_info gauge
   mobile_modem_build_info{pipeserial_version="0.3.0",version="0.1.0-dev"} 1.0
   # HELP mobile_modem_info Information about the mobile modem being monitored, including device path, manufacturer, model, revision and serial number.
   # TYPE mobile_modem_info gauge
   mobile_modem_info{device="/dev/modem-quectel-control",manufacturer="Quectel",model="EC25",revision="EC25EFAR06A06M4G",serial="860548043742078"} 1.0
   mobile_modem_info{device="/dev/modem-huawei-control",manufacturer="Huawei Technologies Co., Ltd.",model="ME909s-120",revision="11.617.15.00.00",serial="864172044791624"} 1.0
   # HELP mobile_modem_atcsq_rssi RSSI for the mobile modem as returned by AT+CSQ
   # TYPE mobile_modem_atcsq_rssi gauge
   mobile_modem_atcsq_rssi{device="/dev/modem-quectel-control"} 31.0
   mobile_modem_atcsq_rssi{device="/dev/modem-huawei-control"} 24.0
   # HELP mobile_modem_atcsq_ber BER for the mobile modem as returned by AT+CSQ
   # TYPE mobile_modem_atcsq_ber gauge
   mobile_modem_atcsq_ber{device="/dev/modem-quectel-control"} 99.0
   mobile_modem_atcsq_ber{device="/dev/modem-huawei-control"} 99.0
   [tykling@container1 ~]$ 


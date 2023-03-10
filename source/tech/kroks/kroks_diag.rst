.. toctree::
    

Диагностика каналов на оборудовании KROKS
=========================================

Подключение к оборудованию производится по адресу loopback через web-браузер или по ssh. Логин tech, пароль стандартный.

.. note:: При смене каких-либо параметров необходимо применить настройки (в web-интерфейсе внизу будет кнопка Применить), при этом сервис, настройки которого были изменены, перезапустится.

Возможности web-интерфейса
-----------------------------------------------

После подключения через браузер откроется страница с системной информацией (название оборудования, модель, аптайм).

.. figure:: _static/kroks-main1.png
    :scale: 70 %
    :align: center


Ниже на этой же странице будут показаны интерфейсы туннелей и адреса на них, а также клиенты, которые получают IP-адрес по услуге Интернет.

.. figure:: _static/kroks-main2.png
    :scale: 70 %
    :align: center


В разделе *Состояние -> Мониторинг* можно ознакомится с загрузкой системы, а также проверить наличие трафика на интерфейсе:

.. figure:: _static/kroks-monitor.png
    :scale: 70 %
    :align: center


Для проверки уровня сигнала мобильной сети необходимо перейти в раздел *Сеть -> Модем*.
Во вкладке Информация можно ознакомится с моделью модема, температурой, режимами работы. На этой же вкладке можно проверить сим-карту: выводится информация о серийном номере сим-карты, качестве сигнала, его уровне и номер базовой станции.

.. figure:: _static/kroks-modem-main.png
    :scale: 70 %
    :align: center

Для подробной информации о сигнале сети рекомендуется открыть вкладку Наведение антенны в этом же разделе.

.. figure:: _static/kroks-antenna.png
    :scale: 70 %
    :align: center


Настройка режимов работы модема и переключение сим-карт производится во вкладке Конфигурация.

.. figure:: _static/kroks-modem-setting1.png
    :scale: 70 %
    :align: center


Здесь можно выбрать, в каком режиме будет работать модем, какие сети и режимы будут в приоритете.

.. figure:: _static/kroks-modem-setting2.png
    :scale: 70 %
    :align: center


Ниже, на этой же странице, можно выбрать, через какую сим-карту будет работать антенна. Обратите внимание, что перед этим сим-карту следует активировать в ЛК оператора. На примере ниже активна сим-карта МТС, но есть возможность выбрать МГФ.

.... warning::
   Обратите внимание, что перед этим сим-карту следует активировать в ЛК оператора. На примере ниже активна сим-карта МТС, но есть возможность выбрать МГФ. 

.. figure:: _static/kroks-sim-switch.png
    :scale: 70 %
    :align: center



Далее рассмотрим раздел с Сеть -> Интерфейсы. Здесь, как можно понять, отображены интерфейсы, которые есть на оборудовании. Обычно это:

  * Два l2tp-туннеля, интерфейс в сторону клиента (eth0)

  * лупбэк антенны, через который можно к ней подключиться удаленно

  * бридж для подключения выездных инженеров по сети wi-fi (скрытая)

  * менеджер модема, который отвечает за подключение к мобильной сети.

Обратите внимание, что интерфейсы gre не используются на оборудовании КРОКС.

Для услуги L2 так же есть eoip-туннели и бридж, который объединяет eoip и eth0.

На этой странице можно проверить статистику на интерфейсах (хоть и ограниченно), поправить настройки на них или перезапустить.

Как получить более подробную статистику по интерфейсам рассмотрим чуть позже в подключении по ssh.

.. figure:: _static/kroks-interfaces.png
    :scale: 70 %
    :align: center


В разделе Сеть -> QoS можно посмотреть и настроить ширину пропускания для клиента.

.. figure:: _static/kroks-qos.png
    :scale: 70 %
    :align: center


Подключение по ssh
-------------------------------

Для подключения к оборудованию по ssh мы будем использовать putty, но можно использовать любой ssh-клиент.
После подключения и ввода пароля откроется консоль с выводом базовой информации и предложением ввода команды.

.. figure:: _static/kroks-ssh.png
    :scale: 70 %
    :align: center

Ниже рассмотрим некоторые команды и их вывод.

**Alias**

Для удобства на кроксах настроены короткие варианты распространенных команд (т.н. alias), полный список можно узнать набрав **alias** в терминале:

.. code-block:: bash

    @test-kroks:~# alias
    info='information'
    00='set00'
    02='set02'
    linkup='set_up'
    03='set03'
    link='showport'
    macs='showmacs'
    port='showport'
    linkdown='set_down'
    0302='set0302'
    0203='set0203'
    ll='ls -alF --color=auto'
    more='less'
    vim='vi'

Коротко об этих командах:

* **info** - очищает экран и выводит базовую информацию как при подключении по ssh;
* **00**, **03**, **02**, **0302**, **0203** - режимы связи модема и приоритеты (00 - автоматически, 03 - LTE, 02 - 3G);
* **link** и **port** - отображает физический статус линка и ошибки на порту;
* **linkdown** / **linkup** - выключить / включить интерфейс;
* **macs** - на услуге L2 отображает мас-адреса подключенных устройств;

**ifconfig**

Вывод информации обо всех интерфейсах, для информации о каком-то одном интерфейсе надо его явно указать, например, ifconfig eth0. Так можно посмотреть статистику по переданным данным на интерфейсе и наличие ошибок на нем (errors, dropped).

.. code-block:: bash

    @test-kroks:~# ifconfig eth0
    eth0    Link encap:Ethernet  HWaddr 0C:EF:AF:D1:24:92
            inet addr:185.138.78.1  Bcast:185.138.78.255  Mask:255.255.255.0
            inet6 addr: fe80::eef:afff:fed1:2492/64 Scope:Link
            UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
            RX packets:16532 errors:0 dropped:10 overruns:0 frame:0
            TX packets:18983 errors:0 dropped:0 overruns:0 carrier:0
            collisions:0 txqueuelen:1000
            RX bytes:2630688 (2.5 MiB)  TX bytes:7941654 (7.5 MiB)
            Interrupt:5
     
    @test-kroks:~# ifconfig wwan0
    wwan0   Link encap:Ethernet  HWaddr AA:A5:99:1C:1F:7B
            inet addr:10.125.77.245  Bcast:10.255.255.255  Mask:255.0.0.0
            inet6 addr: fe80::a8a5:99ff:fe1c:1f7b/64 Scope:Link
            UP BROADCAST RUNNING NOARP MULTICAST  MTU:1500  Metric:1
            RX packets:8051 errors:0 dropped:0 overruns:0 frame:0
            TX packets:7899 errors:0 dropped:0 overruns:0 carrier:0
            collisions:0 txqueuelen:1000
            RX bytes:723881 (706.9 KiB)  TX bytes:1183281 (1.1 MiB) 

**cat /proc/net/dev**
Так же показывает подробную статистику по интерфейсам, но уже в виде таблицы. 

**arp**
Просмотр arp-таблицы


.. code-block:: bash

    @test-kroks:~# arp
    IP address       HW type     Flags      HW address            Mask    Device
    185.138.78.140   0x1        0x2         00:e0:4c:36:00:e9     *       eth0


**ip a**
Информация об ip- и mac-адресации интерфейсов

.. code-block:: bash

    @test-kroks:~# ip a
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
            valid_lft forever preferred_lft forever
        inet 10.9.211.21/32 brd 255.255.255.255 scope global lo
            valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host
            valid_lft forever preferred_lft forever
    2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc hfsc state UNKNOWN qlen 1000
        link/ether 0c:ef:af:d1:24:92 brd ff:ff:ff:ff:ff:ff
        inet 185.138.78.1/24 brd 185.138.78.255 scope global eth0
            valid_lft forever preferred_lft forever
        inet6 fe80::eef:afff:fed1:2492/64 scope link
            valid_lft forever preferred_lft forever

**ip neigh**
Информация о подключенных устройствах

.. code-block:: bash

    @test-kroks:~# ip neigh
    185.138.78.140 dev eth0 lladdr 00:e0:4c:36:00:e9 ref 1 used 0/0/0 probes 1 REACHABLE
    fe80::45c8:bd4a:f099:4537 dev eth0 lladdr 00:e0:4c:36:00:e9 used 0/0/0 probes 0 STALE

**ping**

проверка доступности удаленного узла. По-умолчанию проводится бесконечно, Ctrl+C для остановки

Ключи:

* -s – размер пакета, но пинговать будет на 8 байт больше
* -i – интервал в секундах
* -I – источник, откуда проводится проверка, может быть указан ip или интерфейс

.. code-block:: bash

    @test-kroks:~# ping 185.77.237.185 -s 1400
    PING 185.77.237.185 (185.77.237.185): 1400 data bytes
    1408 bytes from 185.77.237.185: seq=0 ttl=53 time=79.823 ms
    1408 bytes from 185.77.237.185: seq=1 ttl=53 time=66.272 ms
    1408 bytes from 185.77.237.185: seq=2 ttl=53 time=56.102 ms
    1408 bytes from 185.77.237.185: seq=3 ttl=53 time=62.545 ms
    ^C
    --- 185.77.237.185 ping statistics ---
    4 packets transmitted, 4 packets received, 0% packet loss
    round-trip min/avg/max = 56.102/66.185/79.823 ms

**uptime**
Показывает время работы антенны. 

.. code-block:: bash

    @test-kroks:~# uptime
  	    11:29:06 up 28 min,  load average: 2.15, 1.31, 1.04

**reboot**
Немедленная перезагрузка антенны. 

Тестирование пропускной способности
--------------------------------------------------------------------

Тестирование скорости проводится утилитой iperf3, на оборудовании Крокс iperf-сервер автоматически запускается при загрузке системы.

Так как на РУСах, куда терминируются туннели с Крокса, нет технической возможности запустить iperf-клиента, тестирование проводится либо с компьютера специалиста, либо с сервера, для генерации конфигов (bender).

По-умолчанию тестирование проводится протоколом TCP.

Синтаксис выглядит следующим образом:

.. code-block:: bash

    iperf3 -c 10.9.10.10 -b 2M -t 300 -l 1400 -R

Теперь немного о ключах:

* -c - означает что iperf3 будет запущен в качестве клиента и подключится к 10.9.10.10.
* -b - указывает скорость тестирования, в данном примере 2 Мбит/с, если не использовать -b, то ограничения скорости не будет и антенна может потерять связь из-за перегрузки.
* -t - указывает время тестирования в секундах.
* -l - указывает длину отправляемых пакетов, по-умолчанию тестирование проводится протоколом TCP, поэтому ключ не обязателен.
* --bidir - двухстороннее тестирование (прием, отдача)
* -R - reverse, по-умолчанию трафик отправляется от сервера к клиенту (от антенны к компьютеру, с которого тестируют), но ключ -R позволяет проводить тестирование в другую сторону.

Таким образом, для полноценного тестирования пропускной способности, необходимо сначала проверить как канал держит скорость на загрузку, а после этого на отдачу.

Параллельно запуском тестирования, следует запустить пинг с РУСа, куда приземляется антенна, до её loopback'а, чтобы снять показания задержек.

Пример результатов тестирования (вывод команды iperf и статистика задержек с РУСа): 

.. code-block:: bash

    @robot:~$ iperf3 -c 10.9.209.87 -b 10M -l 1450 -t 1000 --bidir
    Connecting to host 10.9.209.87, port 5201
    [  5] local 192.168.10.72 port 37160 connected to 10.9.209.87 port 5201
    [  7] local 192.168.10.72 port 37162 connected to 10.9.209.87 port 5201
    [ ID][Role] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5][TX-C]   0.00-1.00   sec  1.19 MBytes  10.0 Mbits/sec    0   91.5 KBytes
    [  7][RX-C]   0.00-1.00   sec  1.03 MBytes  8.61 Mbits/sec
    [  5][TX-C]   1.00-2.00   sec  1.19 MBytes  10.0 Mbits/sec    0   98.3 KBytes
    [  7][RX-C]   1.00-2.00   sec  1.25 MBytes  10.5 Mbits/sec
    [  5][TX-C]   2.00-3.00   sec  1.19 MBytes  10.0 Mbits/sec    0   98.3 KBytes
    [  7][RX-C]   2.00-3.00   sec  1.30 MBytes  10.9 Mbits/sec
    [  5][TX-C]   3.00-4.00   sec  1.19 MBytes  10.0 Mbits/sec    2   80.5 KBytes
    [  7][RX-C]   3.00-4.00   sec  1.11 MBytes  9.31 Mbits/sec

.. code-block:: bash

    M9-Internet-1] > ping interval=0.5 size=1500 10.9.209.87
      SEQ HOST                                     SIZE TTL TIME  STATUS
        0 10.9.209.87                              1500  64 50ms 
        1 10.9.209.87                              1500  64 48ms 
        2 10.9.209.87                              1500  64 47ms 
        3 10.9.209.87                              1500  64 65ms 
        4 10.9.209.87                              1500  64 47ms 
        5 10.9.209.87                              1500  64 45ms 
        6 10.9.209.87                              1500  64 52ms 
        7 10.9.209.87                              1500  64 61ms 
        8 10.9.209.87                              1500  64 49ms 
        9 10.9.209.87                              1500  64 46ms 
       10 10.9.209.87                              1500  64 86ms 
        sent=11 received=11 packet-loss=0% min-rtt=45ms avg-rtt=54ms max-rtt=86ms
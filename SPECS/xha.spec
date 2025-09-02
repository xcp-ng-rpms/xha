%global package_speccommit 12ac3bfdaad06b8db83feba5ef345b5b252ade91
%global package_srccommit v25.1.0
Summary: xha - XenServer proprietary HA daemon
Name:    xha
Version: 25.1.0
Release: 1%{?xsrel}.1%{?dist}
License: GPLv2
URL:     https://github.com/xenserver/xha
Source0: xha-25.1.0.tar.gz

BuildRequires: gcc
BuildRequires: libxml2-devel
BuildRequires: xen-devel
%{?_cov_buildrequires}

Requires: portreserve

# XCP-ng patches
TODO

%description
This package contains the HA heartbeating daemon used for XenServer's HA feature

%prep
%autosetup -p1
%{?_cov_prepare}

%build
%{?_cov_wrap} make

%install
DESTDIR=$RPM_BUILD_ROOT make install
%{?_cov_install}

%files
%{_sysconfdir}/logrotate.d/xha
%{_sysconfdir}/portreserve/xhad
%{_libexecdir}/xapi/cluster-stack/xhad/calldaemon
%{_libexecdir}/xapi/cluster-stack/xhad/cleanupwatchdog
%{_libexecdir}/xapi/cluster-stack/xhad/dumpstatefile
%{_libexecdir}/xapi/cluster-stack/xhad/ha_clear_excluded
%{_libexecdir}/xapi/cluster-stack/xhad/ha_disarm_fencing
%{_libexecdir}/xapi/cluster-stack/xhad/ha_errnorc
%{_libexecdir}/xapi/cluster-stack/xhad/ha_null
%{_libexecdir}/xapi/cluster-stack/xhad/ha_propose_master
%{_libexecdir}/xapi/cluster-stack/xhad/ha_query_liveset
%{_libexecdir}/xapi/cluster-stack/xhad/ha_rc
%{_libexecdir}/xapi/cluster-stack/xhad/ha_set_excluded
%{_libexecdir}/xapi/cluster-stack/xhad/ha_set_host_weight
%{_libexecdir}/xapi/cluster-stack/xhad/ha_set_pool_state
%{_libexecdir}/xapi/cluster-stack/xhad/ha_start_daemon
%{_libexecdir}/xapi/cluster-stack/xhad/ha_stop_daemon
%{_libexecdir}/xapi/cluster-stack/xhad/weightctl
%{_libexecdir}/xapi/cluster-stack/xhad/writestatefile
%{_libexecdir}/xapi/cluster-stack/xhad/xhad

%{?_cov_results_package}

%changelog
* Tue Sep 02 2025 Ronan Abhamon <ronan.abhamon@vates.tech> - 25.1.0-1.1
- Update to 25.1.0-1
- TODO: Update XCP-ng patches
- *** Upstream changelog ***
  * Thu Mar 06 2025 Gerald Elder-Vass <gerald.elder-vass@cloud.com> - 25.1.0-1
  - CA-407106: Fix various static analyzer warnings
  - CA-404658: Separate heartbeat send and receive threads
  - CA-407313: Replace HA spinlock with rwlock
  - CA-407256: Call to xha-lc is a no-op
  - CA-406953: Fix pointer truncation in hypercall arguments and undefined behaviour
  * Thu Jan 30 2025 Alex Brett <alex.brett@cloud.com> - 25.0.1-1
  - CA-405454: Fix xha when using cgroup v2

* Mon Mar 31 2025 Samuel Verschelde <stormi-xcp@ylix.fr> - 25.0.0-1.1
- Update to 25.0.0-1
- *** Upstream changelog ***
  * Fri Jan 10 2025 Rob Hoes <rob.hoes@citrix.com> - 25.0.0-1
  - CA-403139: Set scheduler policy and priority thread
  - CA-403683: Configurable syslog printing

* Fri Sep 15 2023 Samuel Verschelde <stormi-xcp@ylix.fr> - 10.5.0-1.1
- Update to 10.5.0-1
- Drop xha-10.3.0-support-ipv6.XCP-ng.patch, merged upstream
- *** Upstream changelog ***
- * Wed May 24 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 10.5.0-1
- - lib: ensure the correct maximum amount of hosts
- * Tue Apr 18 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 10.4.0-1
- - CP-41049: Safely remove /proc/xen from dom0
- - feat(heartbeat): support IPv6

* Wed May 10 2023 Benjamin Reis <benjamin.reis@vates.fr> - 10.3.0-3.2
- Add xha-10.3.0-support-ipv6.XCP-ng.patch

* Tue Aug 30 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 10.3.0-3.1
- Rebase on CH 8.3 Preview
- Re-add xha-10.1.0-support-drbd.XCP-ng.patch patch to support DRBD devices

* Thu Dec 09 2021 Rob Hoes <rob.hoes@citrix.com> - 10.3.0-3
- Bump release and rebuild

* Wed Aug 25 2021 Christian Lindig <christian.lindig@citrix.com> - 10.3.0-2
- Bump release and rebuild

* Thu Jul 22 2021 Rachel Yan <Rachel.Yan@citrix.com> - 10.3.0-1
- CA-322009: Fixed warning from set scheduler

* Tue Feb 16 2021 Rob Hoes <rob.hoes@citrix.com> - 10.2.0-1
- CA-351513: fix gcc's -fanalyzer warnings
- maintenance: ignore generated files

* Fri Feb 21 2020 Steven Woods <steven.woods@citrix.com> - 10.1.0-2
- CP33120: Add Coverity build macros

* Mon Jul 01 2019 Christian Lindig <christian.lindig@citrix.com> - 10.1.0-1
- XSI-301: Print errno when watchdog hypercall fails.
- XSI-301: remove duplicated unlock_pages lines
- CA-315962 cleanupwatchdog: Use hypercall's errno
- CA-315962 cleanupwatchdog: exit when encountering errors on hypercalls
- CA-315962 cleanupwatchdog: restrict hypercalls to disable watchdogs
- CA-315962 cleanupwatchdog: simplify hypercall call handling
- CA-315962 cleanupwatchdog: Allow resetting watchdog slots without an HA file
- CA-315962: Flush watchdog slots on HA startup

* Tue Nov 8 2016 Euan Harris <euan.harris@citrix.com> - 10.0.1-1
- Include Git commit metadata in source archive

* Tue Oct 18 2016 Euan Harris <euan.harris@citrix.com> - 10.0.0-1
- Build from GitHub sources

* Mon Oct 17 2016 Vivek Kumar Chaubey <vivekkumar.chaubey@citrix.com> - 7.0.91-248
- Build using transformer

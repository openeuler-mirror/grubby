Name: grubby
Version: 8.40
Release: 26
Summary: Update and display information about the configuration files
License: GPLv2+
URL: https://github.com/rhinstaller/grubby
Source0: https://github.com/rhboot/grubby/archive/%{version}-1.tar.gz
Source1: grubby-bls
Source2: grubby.in
Source3: installkernel.in
Patch1: drop-uboot-uImage-creation.patch
Patch2: 0001-Change-return-type-in-getRootSpecifier.patch
Patch3: 0002-Add-btrfs-subvolume-support-for-grub2.patch
Patch4: 0003-Use-system-LDFLAGS.patch
Patch5: 0004-Honor-sbindir.patch
Patch6: 0005-installkernel-use-kernel-install.patch

Patch6001: Set-envFile-from-env-when-bootloader-is-not-specifie.patch
Patch6002: grubby-properly-handle-mixed-and-and-nested-quotes.patch
Patch6003: Drop-SEGV-handler.patch
Patch6004: Add-a-bunch-of-tests-for-various-default-kernel-titl.patch
Patch6005: Emit-better-systemd-debug-settings-on-debug-entries.patch
Patch6006: Don-t-leak-from-one-extractTitle-call.patch
Patch6007: Fix-dracut-cmdline-options-and-conditionalize-them-t.patch
Patch6008: Always-do-the-rungrubby-debug-after-the-normal-kerne.patch
Patch6009: Be-more-thorough-about-flushing-our-config-file-when.patch
Patch6010: Fix-incorrect-test-case-and-remove-args-with-a-value.patch
Patch6011: grubby-Make-sure-configure-BOOTLOADER-variables-are-.patch
Patch6012: Fix-GCC-warnings-about-possible-string-truncations-a.patch
Patch6013: Check-that-pointers-are-not-NULL-before-dereferencin.patch
Patch6014: Print-default-image-even-if-isn-t-a-suitable-one.patch
Patch6015: backport-Make-SET_VARIABLE-get-handled-individually-in-GetNex.patch

Patch9001: fix-make-test-fail-when-no-boot-partition.patch
Patch9002: Fix-make-test-fail-for-g2-1.15.patch

BuildRequires: gcc pkgconfig glib2-devel popt-devel
BuildRequires: libblkid-devel git-core sed make
BuildRequires: util-linux-ng
%ifarch aarch64 i686 x86_64
BuildRequires: grub2-tools-minimal gdb
Requires: grub2-tools grub2-tools-minimal
%endif

%description
grubby is a command line tool for updating and displaying information about
the configuration files for the grub, lilo, elilo (ia64), yaboot (powerpc)
and zipl (s390) boot loaders. It is primarily designed to be used from scripts
which install new kernels and need to find information about the current boot
environment.

%package bls
Summary:        a command line tool for updating bootloader configs
Conflicts:      %{name} <= 8.40-13
BuildArch:      noarch

%description bls
the package provides a grubby wrapper that manages BootLoaderSpec files and is
meant to only be used for legacy compatibility users with existing grubby users.

%package_help

%prep
%autosetup -n %{name}-%{version}-1 -p1

%build
%make_build

%check
#make test

%install
%make_install mandir=%{_mandir} sbindir=%{_sbindir}

mkdir -p %{buildroot}%{_libexecdir}/{grubby,installkernel}/ %{buildroot}%{_sbindir}/
mv -v %{buildroot}%{_sbindir}/grubby %{buildroot}%{_libexecdir}/grubby/grubby
mv -v %{buildroot}%{_sbindir}/installkernel %{buildroot}%{_libexecdir}/installkernel/installkernel
cp -v %{SOURCE1} %{buildroot}%{_libexecdir}/grubby/
sed -e "s,@@LIBEXECDIR@@,%{_libexecdir}/grubby,g" %{SOURCE2} > %{buildroot}%{_sbindir}/grubby
sed -e "s,@@LIBEXECDIR@@,%{_libexecdir}/installkernel,g" %{SOURCE3} > %{buildroot}%{_sbindir}/installkernel

%pre

%preun

%post

%postun

%files
%license COPYING
%dir %{_libexecdir}/grubby
%dir %{_libexecdir}/installkernel
%attr(0755,root,root) %{_libexecdir}/grubby/grubby
%attr(0755,root,root) %{_libexecdir}/installkernel/installkernel
%attr(0755,root,root) %{_sbindir}/grubby
%attr(0755,root,root) %{_sbindir}/installkernel
%attr(0755,root,root) %{_sbindir}/new-kernel-pkg

%files bls
%dir %{_libexecdir}/grubby
%attr(0755,root,root) %{_libexecdir}/grubby/grubby-bls
%attr(0755,root,root) %{_sbindir}/grubby

%files help
%defattr(-,root,root)
%{_mandir}/man8/*.8*

%changelog
- Thu Jan 1 2021 yangzhuangzhuang <yangzhuangzhuang1@huawei.com> - 8.40-26
- Fix the following problem:The grub.cfg file is modified.As a result,the system fails to start. 

* Mon Nov 2 2020 yixiangzhike <zhangxingliang3@huawei.com> - 8.40-25
- add grub2-tools-minimal to Requires

* Sat Mar 14 2020 openEuler Buildteam <buildteam@openeuler.org> - 8.40-24
- fixbug in self-building

* Mon Dec 30 2019 openEuler Buildteam <buildteam@openeuler.org> - 8.40-23
- Modify patch info

* Sat Nov 30 2019 openEuler Buildteam <buildteam@openeuler.org> - 8.40-22
- add package bls to fix kernel package installation error

* Thu Sep 26 2019 openEuler Buildteam <buildteam@openeuler.org> - 8.40-21
- Modify patch info

* Mon Sep 23 2019 openEuler Buildteam <buildteam@openeuler.org> - 8.40-20
- Modify Requires

* Wed Sep 18 2019 openEuler Buildteam <buildteam@openeuler.org> - 8.40-19
- Package init

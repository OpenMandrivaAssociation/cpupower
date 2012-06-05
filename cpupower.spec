#
# Spec file generated by kdist version v0.4-28-gcada
#
%define name		cpupower
%define version		3.4.1
%define src_uname_r	3.4.1-1
%define source_release	1
%define build_release	1%{nil}
%define archive		cpupower-3.4.1-1.1

%define build_srpm	1
%define no_source	1

%define _source_path	/usr/src/linux-%{src_uname_r}
%if %no_source
%define source_path	%{_source_path}/
%else
%define source_path	./
%endif

%define major		0
%define libname		%mklibname cpupower %{major}
%define devname		%mklibname cpupower -d

# Add "--without doc" option to disable documentation generation
%bcond_without doc

Name:			%{name}
Summary:		The power analysis tools for your processor
URL:			http://www.kernel.org
Group:			System/Kernel and hardware
License:		GPLv2
Version:		%{version}
Release:		%mkrel %{source_release}.%{build_release}
ExclusiveArch:		%{ix86} x86_64
%if %build_srpm
Source:			%{archive}.tar.bz2
%endif
BuildRoot:		%{_tmppath}/%{name}-%{version}-root
%if %no_source
BuildRequires:		kernel-source = %{version}-%{mkrel %{source_release}}
%endif
BuildRequires:		pciutils-devel
%ifarch %ix86
Buildrequires:		liblrmi0-devel
%endif
%description
cpupower is a collection of tools to examine and tune power saving
related features of your processor.

This collection of tools allow users and developers to have *one* tool
to get an overview what their system supports and to monitor and debug
CPU power management in detail.


%package -n %{libname}
Summary:		The shared library for %{name}
Group:			System/Kernel and hardware

%description -n %{libname}
"libcpupower" is a library which offers a unified access method for
userspace tools and programs to the cpufreq core and drivers in the
Linux kernel. This allows for code reduction in userspace tools, a
clean implementation of the interaction to the cpufreq core, and
support for both the sysfs and proc interfaces.


%package -n %{devname}
Summary:		The development files for %{name} shared library
Group:			System/Kernel and hardware
Requires:		%{libname} = %{version}-%{release}
Provides:		cpupower-devel = %{version}-%{release}

%description -n %{devname}
The development files needed for cpupower's shared library.

"libcpupower" is a library which offers a unified access method for
userspace tools and programs to the cpufreq core and drivers in the
Linux kernel. This allows for code reduction in userspace tools, a
clean implementation of the interaction to the cpufreq core, and
support for both the sysfs and proc interfaces.

%if %no_source
%define outdir_opt	O=$(pwd)
%endif

%global __cpupower_make	make %{?_smp_mflags} -C %{source_path}tools/power/%{name}
%global _cpupower_make	%{__cpupower_make} bindir=%{_bindir} libdir=%{_libdir} mandir=%{_mandir}
%global cpupower_make	%{_cpupower_make} %{?outdir_opt} DESTDIR=%{buildroot} CPUFREQ_BENCH=false

%if %build_srpm
%prep
%setup -q -n %{archive}
%endif
# when reusing the kernel source, the empty archive misses the
# README, so import it in that case.
test -f README || cp %{source_path}tools/power/%{name}/README .

# We're rebuilding in any cases (srpm or rpm) since the flags passed
# to make are not the same as the ones used by the user previously.
%build
%{cpupower_make}
%ifarch %ix86
%{cpupower_make} -C debug/i386
%endif
%ifarch x86_64
%{cpupower_make} -C debug/x86_64
%endif

%install
%{cpupower_make} install-lib install-tools
%if %{with doc}
%{cpupower_make} install-man
%endif
%ifarch %ix86
%{cpupower_make} -C debug/i386 install
%endif
%ifarch x86_64
%{cpupower_make} -C debug/x86_64 install
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/cpupower
%{_bindir}/centrino-decode
%{_bindir}/powernow-k8-decode
%if %{with doc}
%{_mandir}/man[1-8]/cpupower*
%endif
%ifarch %ix86
%{_bindir}/dump_psb
%{_bindir}/intel_gsic
%endif
%files -n %{libname}
%doc README
%{_libdir}/libcpupower.so.%{major}*

%files -n %{devname}
%doc README
%{_includedir}/cpufreq.h
%{_libdir}/libcpupower.so

%changelog
* Tue Jun 05 2012 Franck Bui <franck.bui@mandriva.com> 
  + Mandriva Release v3.4.1-1
  + radio-rtrack: fix build error (implicit declaration of function 'kzalloc')
  + [overlayfs] switch to use inode_only_permissions
  + [overlayfs] inode_only_permission: export inode level permissions checks
  + [overlayfs] update touch_atime() usage (3.4 build fix)
  + [overlayfs] switch from d_alloc_root() to d_make_root() (3.4 build fix)
  + [overlayfs] follow header cleanup (3.4 build fix)
  + [overlayfs] fs: limit filesystem stacking depth
  + [overlayfs] overlay filesystem documentation
  + [overlayfs] implement show_options
  + [overlayfs] add statfs support
  + [overlayfs] overlay filesystem
  + [overlayfs] vfs: introduce clone_private_mount()
  + [overlayfs] vfs: export do_splice_direct() to modules
  + [overlayfs] vfs: add i_op->open()
  + [overlayfs] vfs: pass struct path to __dentry_open()
  + usb: ehci: make HC see up-to-date qh/qtd descriptor ASAP
  + Mandriva Linux boot logo.
  + media video pwc lie in proc usb devices
  + usb storage unusual_devs add id 2.6.37 buildfix
  + Change to usb storage of unusual_dev.
  + Add blacklist of usb hid modules
  + bluetooth hci_usb disable isoc transfers
  + sound alsa hda ad1884a hp dc model
  + Support a Bluetooth SCO.
  + Include kbuild export pci_ids
  + platform x86 add shuttle wmi driver
  + net netfilter psd 2.6.35 buildfix
  + ipt_psd: Mandriva changes
  + net netfilter psd
  + net netfilter IFWLOG 2.6.37 buildfix
  + IFWLOG netfilter: fix return value of ipt_IFWLOG_checkentry()
  + net netfilter IFWLOG 2.6.35 buildfix
  + netfilter ipt_IFWLOG: Mandriva changes
  + net netfilter IFWLOG
  + net sis190 fix list usage
  + gpu drm mach64 3.3 buildfix
  + gpu drm mach64 3.2 buildfix
  + gpu drm mach64 2.6.39 buildfix
  + gpu drm mach64 2.6.37 buildfix
  + gpu drm mach64 2.6.36 buildfix
  + gpu drm mach64 fix for changed drm_ioctl
  + gpu drm mach64 fix for changed drm_pci_alloc
  + gpu drm mach64 2.6.31 buildfix
  + gpu drm mach64 fixes
  + gpu drm mach64
  + agp/intel: add new host bridge id for Q57 system
  + mpt scsi modules for VMWare's emulated
  + ppscsi: build fix for 2.6.39
  + scsi megaraid new sysfs name
  + scsi ppscsi mdvbz45393
  + scsi ppscsi update for scsi_data_buffer
  + scsi ppscsi sg helper update
  + scsi ppscsi_fixes
  + scsi ppscsi-2.6.2
  + acpi video add blacklist to use vendor driver
  + acpi processor M720SR limit to C2
  + CLEVO M360S acpi irq workaround
  + acpi add proc event regs
  + acpi dsdt initrd v0.9c fixes
  + ACPI: initramfs DSDT override support
  + UBUNTU: SAUCE: isapnp_init: make isa PNP scans occur async
  + pnp pnpbios off by default
  + PCI: Add ALI M5229 IDE comaptibility mode quirk
  + Card bus's PCI last bus
  + x86, cpufreq: set reasonable default for scaling_min_freq with p4-clockmod
  + x86 cpufreq speedstep dothan 3
  + x86 boot video 80x25 if break
  + x86 pci toshiba equium a60 assign busses
  + kdist: make the config name part of the localversion
  + kdist: give a name to the config file

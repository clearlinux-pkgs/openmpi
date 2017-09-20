#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openmpi
Version  : 2.1.1
Release  : 8
URL      : https://www.open-mpi.org/software/ompi/v2.1/downloads/openmpi-2.1.1.tar.bz2
Source0  : https://www.open-mpi.org/software/ompi/v2.1/downloads/openmpi-2.1.1.tar.bz2
Summary  : A powerful implementation of MPI/SHMEM
Group    : Development/Tools
License  : BSD-3-Clause
Requires: openmpi-bin
Requires: openmpi-lib
Requires: openmpi-doc
Requires: openmpi-data
BuildRequires : db-dev
BuildRequires : flex
BuildRequires : grep
BuildRequires : hwloc-dev
BuildRequires : libpciaccess-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(zlib)
BuildRequires : sed
BuildRequires : systemd-dev
Patch1: root.patch
Patch2: lfence.patch
Patch3: noyield.patch

%description
Open MPI is an open source implementation of the Message Passing
Interface specification (http://www.mpi-forum.org/) developed and
maintained by a consortium of research, academic, and industry
partners.

Open MPI also includes an implementation of the OpenSHMEM parallel
programming API (http://www.openshmem.org/).  OpenSHMEM is a
Partitioned Global Address Space (PGAS) abstraction layer, which
provides fast inter-process communication using one-sided
communication techniques.

This RPM contains all the tools necessary to compile, link, and run
Open MPI and OpenSHMEM jobs.

%package bin
Summary: bin components for the openmpi package.
Group: Binaries
Requires: openmpi-data

%description bin
bin components for the openmpi package.


%package data
Summary: data components for the openmpi package.
Group: Data

%description data
data components for the openmpi package.


%package dev
Summary: dev components for the openmpi package.
Group: Development
Requires: openmpi-lib
Requires: openmpi-bin
Requires: openmpi-data
Provides: openmpi-devel

%description dev
dev components for the openmpi package.


%package doc
Summary: doc components for the openmpi package.
Group: Documentation

%description doc
doc components for the openmpi package.


%package lib
Summary: lib components for the openmpi package.
Group: Libraries
Requires: openmpi-data

%description lib
lib components for the openmpi package.


%prep
%setup -q -n openmpi-2.1.1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505925984
export CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error   -Wl,-z,max-page-size=0x1000 -m64 -march=westmere -mtune=haswell"
export CXXFLAGS=$CFLAGS
unset LDFLAGS
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static --enable-branch-probabilities \
--enable-builtin-atomics \
--with-wrapper-cflags-prefix="-march=native -O3" \
--with-wrapper-cxxflags-prefix="-march=native -O3"
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1505925984
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/mpi.mod
/usr/lib64/mpi_ext.mod
/usr/lib64/mpi_f08.mod
/usr/lib64/mpi_f08_callbacks.mod
/usr/lib64/mpi_f08_ext.mod
/usr/lib64/mpi_f08_interfaces.mod
/usr/lib64/mpi_f08_interfaces_callbacks.mod
/usr/lib64/mpi_f08_types.mod
/usr/lib64/pmpi_f08_interfaces.mod

%files bin
%defattr(-,root,root,-)
/usr/bin/mpiCC
/usr/bin/mpic++
/usr/bin/mpicc
/usr/bin/mpicxx
/usr/bin/mpiexec
/usr/bin/mpif77
/usr/bin/mpif90
/usr/bin/mpifort
/usr/bin/mpirun
/usr/bin/ompi-clean
/usr/bin/ompi-dvm
/usr/bin/ompi-ps
/usr/bin/ompi-server
/usr/bin/ompi-submit
/usr/bin/ompi-top
/usr/bin/ompi_info
/usr/bin/opal_wrapper
/usr/bin/orte-clean
/usr/bin/orte-dvm
/usr/bin/orte-info
/usr/bin/orte-ps
/usr/bin/orte-server
/usr/bin/orte-submit
/usr/bin/orte-top
/usr/bin/ortecc
/usr/bin/orted
/usr/bin/orterun
/usr/bin/oshcc
/usr/bin/oshfort
/usr/bin/oshmem_info
/usr/bin/oshrun
/usr/bin/shmemcc
/usr/bin/shmemfort
/usr/bin/shmemrun

%files data
%defattr(-,root,root,-)
/usr/share/openmpi/amca-param-sets/example.conf
/usr/share/openmpi/help-btl-vader.txt
/usr/share/openmpi/help-coll-sync.txt
/usr/share/openmpi/help-dash-host.txt
/usr/share/openmpi/help-errmgr-base.txt
/usr/share/openmpi/help-ess-base.txt
/usr/share/openmpi/help-ess-hnp.txt
/usr/share/openmpi/help-hostfile.txt
/usr/share/openmpi/help-mca-base.txt
/usr/share/openmpi/help-mca-bml-r2.txt
/usr/share/openmpi/help-mca-coll-base.txt
/usr/share/openmpi/help-mca-osc-base.txt
/usr/share/openmpi/help-mca-var.txt
/usr/share/openmpi/help-mpi-api.txt
/usr/share/openmpi/help-mpi-btl-base.txt
/usr/share/openmpi/help-mpi-btl-sm.txt
/usr/share/openmpi/help-mpi-btl-tcp.txt
/usr/share/openmpi/help-mpi-coll-sm.txt
/usr/share/openmpi/help-mpi-common-sm.txt
/usr/share/openmpi/help-mpi-errors.txt
/usr/share/openmpi/help-mpi-pml-ob1.txt
/usr/share/openmpi/help-mpi-runtime.txt
/usr/share/openmpi/help-mpool-base.txt
/usr/share/openmpi/help-oob-base.txt
/usr/share/openmpi/help-oob-tcp.txt
/usr/share/openmpi/help-opal-hwloc-base.txt
/usr/share/openmpi/help-opal-runtime.txt
/usr/share/openmpi/help-opal-shmem-mmap.txt
/usr/share/openmpi/help-opal-shmem-posix.txt
/usr/share/openmpi/help-opal-shmem-sysv.txt
/usr/share/openmpi/help-opal-timer-linux.txt
/usr/share/openmpi/help-opal-util.txt
/usr/share/openmpi/help-opal-wrapper.txt
/usr/share/openmpi/help-opal_info.txt
/usr/share/openmpi/help-orte-clean.txt
/usr/share/openmpi/help-orte-filem-raw.txt
/usr/share/openmpi/help-orte-info.txt
/usr/share/openmpi/help-orte-odls-base.txt
/usr/share/openmpi/help-orte-odls-default.txt
/usr/share/openmpi/help-orte-ps.txt
/usr/share/openmpi/help-orte-rmaps-base.txt
/usr/share/openmpi/help-orte-rmaps-md.txt
/usr/share/openmpi/help-orte-rmaps-ppr.txt
/usr/share/openmpi/help-orte-rmaps-resilient.txt
/usr/share/openmpi/help-orte-rmaps-rr.txt
/usr/share/openmpi/help-orte-rmaps-seq.txt
/usr/share/openmpi/help-orte-rtc-base.txt
/usr/share/openmpi/help-orte-runtime.txt
/usr/share/openmpi/help-orte-server.txt
/usr/share/openmpi/help-orte-top.txt
/usr/share/openmpi/help-orted.txt
/usr/share/openmpi/help-orterun.txt
/usr/share/openmpi/help-oshmem-info.txt
/usr/share/openmpi/help-oshmem-memheap.txt
/usr/share/openmpi/help-oshmem-spml-yoda.txt
/usr/share/openmpi/help-oshmem-sshmem-mmap.txt
/usr/share/openmpi/help-oshmem-sshmem-sysv.txt
/usr/share/openmpi/help-oshmem-sshmem.txt
/usr/share/openmpi/help-plm-base.txt
/usr/share/openmpi/help-plm-rsh.txt
/usr/share/openmpi/help-plm-slurm.txt
/usr/share/openmpi/help-pmix-base.txt
/usr/share/openmpi/help-ras-base.txt
/usr/share/openmpi/help-ras-simulator.txt
/usr/share/openmpi/help-ras-slurm.txt
/usr/share/openmpi/help-rcache-base.txt
/usr/share/openmpi/help-regex.txt
/usr/share/openmpi/help-rmaps_rank_file.txt
/usr/share/openmpi/help-rtc-freq.txt
/usr/share/openmpi/help-shmem-api.txt
/usr/share/openmpi/help-shmem-runtime.txt
/usr/share/openmpi/help-state-staged-hnp.txt
/usr/share/openmpi/mpiCC-wrapper-data.txt
/usr/share/openmpi/mpic++-wrapper-data.txt
/usr/share/openmpi/mpicc-wrapper-data.txt
/usr/share/openmpi/mpicxx-wrapper-data.txt
/usr/share/openmpi/mpif77-wrapper-data.txt
/usr/share/openmpi/mpif90-wrapper-data.txt
/usr/share/openmpi/mpifort-wrapper-data.txt
/usr/share/openmpi/openmpi-valgrind.supp
/usr/share/openmpi/ortecc-wrapper-data.txt
/usr/share/openmpi/oshcc-wrapper-data.txt
/usr/share/openmpi/oshfort-wrapper-data.txt
/usr/share/openmpi/shmemcc-wrapper-data.txt
/usr/share/openmpi/shmemfort-wrapper-data.txt

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/mpp/shmem.fh
/usr/include/mpp/shmem.h
/usr/include/openmpi/ompi/mpiext/affinity/c/mpiext_affinity_c.h
/usr/include/openmpi/ompi/mpiext/cuda/c/mpiext_cuda_c.h
/usr/include/openshmem/oshmem/constants.h
/usr/include/openshmem/oshmem/frameworks.h
/usr/include/openshmem/oshmem/types.h
/usr/include/openshmem/oshmem/version.h
/usr/include/openshmem/oshmem_config.h
/usr/include/shmem.fh
/usr/lib64/libmca_common_sm.so
/usr/lib64/libmpi.so
/usr/lib64/libmpi_mpifh.so
/usr/lib64/libmpi_usempi_ignore_tkr.so
/usr/lib64/libmpi_usempif08.so
/usr/lib64/libompitrace.so
/usr/lib64/libopen-pal.so
/usr/lib64/libopen-rte.so
/usr/lib64/liboshmem.so
/usr/lib64/pkgconfig/ompi-c.pc
/usr/lib64/pkgconfig/ompi-cxx.pc
/usr/lib64/pkgconfig/ompi-f77.pc
/usr/lib64/pkgconfig/ompi-f90.pc
/usr/lib64/pkgconfig/ompi-fort.pc
/usr/lib64/pkgconfig/ompi.pc
/usr/lib64/pkgconfig/orte.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*
%doc /usr/share/man/man7/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmca_common_sm.so.20
/usr/lib64/libmca_common_sm.so.20.10.1
/usr/lib64/libmpi.so.20
/usr/lib64/libmpi.so.20.10.1
/usr/lib64/libmpi_mpifh.so.20
/usr/lib64/libmpi_mpifh.so.20.11.0
/usr/lib64/libmpi_usempi_ignore_tkr.so.20
/usr/lib64/libmpi_usempi_ignore_tkr.so.20.10.0
/usr/lib64/libmpi_usempif08.so.20
/usr/lib64/libmpi_usempif08.so.20.10.0
/usr/lib64/libompitrace.so.20
/usr/lib64/libompitrace.so.20.10.0
/usr/lib64/libopen-pal.so.20
/usr/lib64/libopen-pal.so.20.10.1
/usr/lib64/libopen-rte.so.20
/usr/lib64/libopen-rte.so.20.10.1
/usr/lib64/liboshmem.so.20
/usr/lib64/liboshmem.so.20.10.1
/usr/lib64/openmpi/libompi_dbg_msgq.so
/usr/lib64/openmpi/mca_allocator_basic.so
/usr/lib64/openmpi/mca_allocator_bucket.so
/usr/lib64/openmpi/mca_atomic_basic.so
/usr/lib64/openmpi/mca_bml_r2.so
/usr/lib64/openmpi/mca_btl_self.so
/usr/lib64/openmpi/mca_btl_sm.so
/usr/lib64/openmpi/mca_btl_tcp.so
/usr/lib64/openmpi/mca_btl_vader.so
/usr/lib64/openmpi/mca_coll_basic.so
/usr/lib64/openmpi/mca_coll_inter.so
/usr/lib64/openmpi/mca_coll_libnbc.so
/usr/lib64/openmpi/mca_coll_self.so
/usr/lib64/openmpi/mca_coll_sm.so
/usr/lib64/openmpi/mca_coll_sync.so
/usr/lib64/openmpi/mca_coll_tuned.so
/usr/lib64/openmpi/mca_dfs_app.so
/usr/lib64/openmpi/mca_dfs_orted.so
/usr/lib64/openmpi/mca_dfs_test.so
/usr/lib64/openmpi/mca_errmgr_default_app.so
/usr/lib64/openmpi/mca_errmgr_default_hnp.so
/usr/lib64/openmpi/mca_errmgr_default_orted.so
/usr/lib64/openmpi/mca_errmgr_default_tool.so
/usr/lib64/openmpi/mca_ess_env.so
/usr/lib64/openmpi/mca_ess_hnp.so
/usr/lib64/openmpi/mca_ess_pmi.so
/usr/lib64/openmpi/mca_ess_singleton.so
/usr/lib64/openmpi/mca_ess_slurm.so
/usr/lib64/openmpi/mca_ess_tool.so
/usr/lib64/openmpi/mca_fbtl_posix.so
/usr/lib64/openmpi/mca_fcoll_dynamic.so
/usr/lib64/openmpi/mca_fcoll_dynamic_gen2.so
/usr/lib64/openmpi/mca_fcoll_individual.so
/usr/lib64/openmpi/mca_fcoll_static.so
/usr/lib64/openmpi/mca_fcoll_two_phase.so
/usr/lib64/openmpi/mca_filem_raw.so
/usr/lib64/openmpi/mca_fs_ufs.so
/usr/lib64/openmpi/mca_grpcomm_direct.so
/usr/lib64/openmpi/mca_io_ompio.so
/usr/lib64/openmpi/mca_io_romio314.so
/usr/lib64/openmpi/mca_iof_hnp.so
/usr/lib64/openmpi/mca_iof_mr_hnp.so
/usr/lib64/openmpi/mca_iof_mr_orted.so
/usr/lib64/openmpi/mca_iof_orted.so
/usr/lib64/openmpi/mca_iof_tool.so
/usr/lib64/openmpi/mca_memheap_buddy.so
/usr/lib64/openmpi/mca_memheap_ptmalloc.so
/usr/lib64/openmpi/mca_mpool_hugepage.so
/usr/lib64/openmpi/mca_notifier_syslog.so
/usr/lib64/openmpi/mca_odls_default.so
/usr/lib64/openmpi/mca_oob_tcp.so
/usr/lib64/openmpi/mca_oob_usock.so
/usr/lib64/openmpi/mca_osc_pt2pt.so
/usr/lib64/openmpi/mca_osc_rdma.so
/usr/lib64/openmpi/mca_osc_sm.so
/usr/lib64/openmpi/mca_patcher_overwrite.so
/usr/lib64/openmpi/mca_plm_isolated.so
/usr/lib64/openmpi/mca_plm_rsh.so
/usr/lib64/openmpi/mca_plm_slurm.so
/usr/lib64/openmpi/mca_pmix_pmix112.so
/usr/lib64/openmpi/mca_pml_cm.so
/usr/lib64/openmpi/mca_pml_ob1.so
/usr/lib64/openmpi/mca_pstat_linux.so
/usr/lib64/openmpi/mca_ras_loadleveler.so
/usr/lib64/openmpi/mca_ras_simulator.so
/usr/lib64/openmpi/mca_ras_slurm.so
/usr/lib64/openmpi/mca_rcache_grdma.so
/usr/lib64/openmpi/mca_rmaps_mindist.so
/usr/lib64/openmpi/mca_rmaps_ppr.so
/usr/lib64/openmpi/mca_rmaps_rank_file.so
/usr/lib64/openmpi/mca_rmaps_resilient.so
/usr/lib64/openmpi/mca_rmaps_round_robin.so
/usr/lib64/openmpi/mca_rmaps_seq.so
/usr/lib64/openmpi/mca_rmaps_staged.so
/usr/lib64/openmpi/mca_rml_oob.so
/usr/lib64/openmpi/mca_routed_binomial.so
/usr/lib64/openmpi/mca_routed_debruijn.so
/usr/lib64/openmpi/mca_routed_direct.so
/usr/lib64/openmpi/mca_routed_radix.so
/usr/lib64/openmpi/mca_rtc_freq.so
/usr/lib64/openmpi/mca_rtc_hwloc.so
/usr/lib64/openmpi/mca_schizo_ompi.so
/usr/lib64/openmpi/mca_scoll_basic.so
/usr/lib64/openmpi/mca_scoll_mpi.so
/usr/lib64/openmpi/mca_sec_basic.so
/usr/lib64/openmpi/mca_sharedfp_individual.so
/usr/lib64/openmpi/mca_sharedfp_lockedfile.so
/usr/lib64/openmpi/mca_sharedfp_sm.so
/usr/lib64/openmpi/mca_shmem_mmap.so
/usr/lib64/openmpi/mca_shmem_posix.so
/usr/lib64/openmpi/mca_shmem_sysv.so
/usr/lib64/openmpi/mca_spml_yoda.so
/usr/lib64/openmpi/mca_sshmem_mmap.so
/usr/lib64/openmpi/mca_sshmem_sysv.so
/usr/lib64/openmpi/mca_state_app.so
/usr/lib64/openmpi/mca_state_dvm.so
/usr/lib64/openmpi/mca_state_hnp.so
/usr/lib64/openmpi/mca_state_novm.so
/usr/lib64/openmpi/mca_state_orted.so
/usr/lib64/openmpi/mca_state_staged_hnp.so
/usr/lib64/openmpi/mca_state_staged_orted.so
/usr/lib64/openmpi/mca_state_tool.so
/usr/lib64/openmpi/mca_topo_basic.so
/usr/lib64/openmpi/mca_vprotocol_pessimist.so
#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openmpi
Version  : 4.1.3
Release  : 46
URL      : https://download.open-mpi.org/release/open-mpi/v4.1/openmpi-4.1.3.tar.gz
Source0  : https://download.open-mpi.org/release/open-mpi/v4.1/openmpi-4.1.3.tar.gz
Source1  : openmpi
Summary  : An extended/exascale implementation of PMI
Group    : Development/Tools
License  : BSD-3-Clause CECILL-1.1
Requires: openmpi-bin = %{version}-%{release}
Requires: openmpi-data = %{version}-%{release}
Requires: openmpi-filemap = %{version}-%{release}
Requires: openmpi-lib = %{version}-%{release}
Requires: openmpi-license = %{version}-%{release}
Requires: openmpi-man = %{version}-%{release}
BuildRequires : flex
BuildRequires : gfortran
BuildRequires : grep
BuildRequires : hwloc-dev
BuildRequires : libevent-dev
BuildRequires : libpciaccess-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(zlib)
BuildRequires : pmix-dev
BuildRequires : sed
BuildRequires : systemd-dev
BuildRequires : valgrind
Patch1: rdtsc.patch
Patch2: stateless.patch

%description
The Process Management Interface (PMI) has been used for quite some time as a
means of exchanging wireup information needed for interprocess communication. Two
versions (PMI-1 and PMI-2) have been released as part of the MPICH effort. While
PMI-2 demonstrates better scaling properties than its PMI-1 predecessor, attaining
rapid launch and wireup of the roughly 1M processes executing across 100k nodes
expected for exascale operations remains challenging.

PMI Exascale (PMIx) represents an attempt to resolve these questions by providing
an extended version of the PMI standard specifically designed to support clusters
up to and including exascale sizes. The overall objective of the project is not to
branch the existing pseudo-standard definitions - in fact, PMIx fully supports both
of the existing PMI-1 and PMI-2 APIs - but rather to (a) augment and extend those
APIs to eliminate some current restrictions that impact scalability, and (b) provide
a reference implementation of the PMI-server that demonstrates the desired level of
scalability.

%package bin
Summary: bin components for the openmpi package.
Group: Binaries
Requires: openmpi-data = %{version}-%{release}
Requires: openmpi-license = %{version}-%{release}
Requires: openmpi-filemap = %{version}-%{release}

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
Requires: openmpi-lib = %{version}-%{release}
Requires: openmpi-bin = %{version}-%{release}
Requires: openmpi-data = %{version}-%{release}
Provides: openmpi-devel = %{version}-%{release}
Requires: openmpi = %{version}-%{release}

%description dev
dev components for the openmpi package.


%package filemap
Summary: filemap components for the openmpi package.
Group: Default

%description filemap
filemap components for the openmpi package.


%package lib
Summary: lib components for the openmpi package.
Group: Libraries
Requires: openmpi-data = %{version}-%{release}
Requires: openmpi-license = %{version}-%{release}
Requires: openmpi-filemap = %{version}-%{release}

%description lib
lib components for the openmpi package.


%package license
Summary: license components for the openmpi package.
Group: Default

%description license
license components for the openmpi package.


%package man
Summary: man components for the openmpi package.
Group: Default

%description man
man components for the openmpi package.


%prep
%setup -q -n openmpi-4.1.3
cd %{_builddir}/openmpi-4.1.3
%patch1 -p1
%patch2 -p1
pushd ..
cp -a openmpi-4.1.3 buildavx2
popd
pushd ..
cp -a openmpi-4.1.3 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1648771254
export GCC_IGNORE_WERROR=1
export CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x1000 -march=westmere -mtune=haswell"
export CXXFLAGS=$CFLAGS
export FFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wno-error -Wl,-z,max-page-size=0x1000 -march=westmere -mtune=haswell"
export FCFLAGS=$FFLAGS
unset LDFLAGS
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
%configure --disable-static --enable-branch-probabilities \
--enable-builtin-atomics \
--with-wrapper-cflags-prefix="-O3" \
--with-wrapper-cxxflags-prefix="-O3" \
--with-wrapper-fcflags-prefix="-O3" \
--with-pmix=external \
--with-libevent=external \
--with-hwloc=external
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static --enable-branch-probabilities \
--enable-builtin-atomics \
--with-wrapper-cflags-prefix="-O3" \
--with-wrapper-cxxflags-prefix="-O3" \
--with-wrapper-fcflags-prefix="-O3" \
--with-pmix=external \
--with-libevent=external \
--with-hwloc=external --with-wrapper-cflags-prefix="-O3 -march=x86-64-v3" \
--with-wrapper-cxxflags-prefix="-O3 -march=x86-64-v3" \
--with-wrapper-fcflags-prefix="-O3 -march=x86-64-v3"
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256 -Wl,-z,x86-64-v4"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256 -Wl,-z,x86-64-v4"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v4"
%configure --disable-static --enable-branch-probabilities \
--enable-builtin-atomics \
--with-wrapper-cflags-prefix="-O3" \
--with-wrapper-cxxflags-prefix="-O3" \
--with-wrapper-fcflags-prefix="-O3" \
--with-pmix=external \
--with-libevent=external \
--with-hwloc=external --with-wrapper-cflags-prefix="-O3 -march=x86-64-v4" \
--with-wrapper-cxxflags-prefix="-O3 -march=x86-64-v4" \
--with-wrapper-fcflags-prefix="-O3 -march=x86-64-v4"
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :
cd ../buildavx512;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1648771254
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/openmpi
cp %{_builddir}/openmpi-4.1.3/LICENSE %{buildroot}/usr/share/package-licenses/openmpi/2530bd3ed2c1661445dacd664b277d1f092c56f3
cp %{_builddir}/openmpi-4.1.3/contrib/dist/mofed/debian/copyright %{buildroot}/usr/share/package-licenses/openmpi/2530bd3ed2c1661445dacd664b277d1f092c56f3
cp %{_builddir}/openmpi-4.1.3/ompi/mca/topo/treematch/treematch/COPYING %{buildroot}/usr/share/package-licenses/openmpi/1d219195f5b198de4d80822b54ee0511f0d38361
cp %{_builddir}/openmpi-4.1.3/ompi/mca/topo/treematch/treematch/LICENSE %{buildroot}/usr/share/package-licenses/openmpi/80be8a39adf3f4419e3f7153aba2ae318eeec910
cp %{_builddir}/openmpi-4.1.3/opal/mca/event/libevent2022/libevent/LICENSE %{buildroot}/usr/share/package-licenses/openmpi/458149cf961c544a997c5de2d3df83cab6e2c08c
cp %{_builddir}/openmpi-4.1.3/opal/mca/hwloc/hwloc201/hwloc/COPYING %{buildroot}/usr/share/package-licenses/openmpi/23ae9dd3b06c170d1abfbdf517a2e4fea90b7cdd
cp %{_builddir}/openmpi-4.1.3/opal/mca/pmix/pmix3x/pmix/LICENSE %{buildroot}/usr/share/package-licenses/openmpi/c0fb365dcaaae482fe7c3673c97d0e8c6d21636d
pushd ../buildavx2/
%make_install_v3
popd
pushd ../buildavx512/
%make_install_v4
popd
%make_install
mkdir -p %{buildroot}/usr/share/modules/modulefiles
install -m 0644 -p %{_sourcedir}/openmpi %{buildroot}/usr/share/modules/modulefiles/
## install_append content
mkdir -p %{buildroot}/usr/share/defaults/etc/openmpi
cp -p %{buildroot}/etc/* %{buildroot}/usr/share/defaults/etc/openmpi/
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/bin/aggregate_profile.pl
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
/usr/bin/ompi-server
/usr/bin/ompi_info
/usr/bin/opal_wrapper
/usr/bin/orte-clean
/usr/bin/orte-info
/usr/bin/orte-server
/usr/bin/ortecc
/usr/bin/orted
/usr/bin/orterun
/usr/bin/profile2mat.pl
/usr/share/clear/optimized-elf/bin*

%files data
%defattr(-,root,root,-)
/usr/share/defaults/etc/openmpi/openmpi-default-hostfile
/usr/share/defaults/etc/openmpi/openmpi-mca-params.conf
/usr/share/defaults/etc/openmpi/openmpi-totalview.tcl
/usr/share/modules/modulefiles/openmpi
/usr/share/openmpi/amca-param-sets/example.conf
/usr/share/openmpi/help-btl-vader.txt
/usr/share/openmpi/help-coll-sync.txt
/usr/share/openmpi/help-dash-host.txt
/usr/share/openmpi/help-errmgr-base.txt
/usr/share/openmpi/help-ess-base.txt
/usr/share/openmpi/help-hostfile.txt
/usr/share/openmpi/help-mca-base.txt
/usr/share/openmpi/help-mca-bml-r2.txt
/usr/share/openmpi/help-mca-coll-base.txt
/usr/share/openmpi/help-mca-hook-base.txt
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
/usr/share/openmpi/help-opal-crs-none.txt
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
/usr/share/openmpi/help-orte-odls-pspawn.txt
/usr/share/openmpi/help-orte-rmaps-base.txt
/usr/share/openmpi/help-orte-rmaps-md.txt
/usr/share/openmpi/help-orte-rmaps-ppr.txt
/usr/share/openmpi/help-orte-rmaps-resilient.txt
/usr/share/openmpi/help-orte-rmaps-rr.txt
/usr/share/openmpi/help-orte-rmaps-seq.txt
/usr/share/openmpi/help-orte-rtc-base.txt
/usr/share/openmpi/help-orte-rtc-hwloc.txt
/usr/share/openmpi/help-orte-runtime.txt
/usr/share/openmpi/help-orte-server.txt
/usr/share/openmpi/help-orte-snapc-base.txt
/usr/share/openmpi/help-orted.txt
/usr/share/openmpi/help-orterun.txt
/usr/share/openmpi/help-osc-pt2pt.txt
/usr/share/openmpi/help-plm-base.txt
/usr/share/openmpi/help-plm-rsh.txt
/usr/share/openmpi/help-plm-slurm.txt
/usr/share/openmpi/help-pmix-base.txt
/usr/share/openmpi/help-pmix-ext3x.txt
/usr/share/openmpi/help-ras-base.txt
/usr/share/openmpi/help-ras-simulator.txt
/usr/share/openmpi/help-ras-slurm.txt
/usr/share/openmpi/help-rcache-base.txt
/usr/share/openmpi/help-regex.txt
/usr/share/openmpi/help-rmaps_rank_file.txt
/usr/share/openmpi/help-state-base.txt
/usr/share/openmpi/mpiCC-wrapper-data.txt
/usr/share/openmpi/mpic++-wrapper-data.txt
/usr/share/openmpi/mpicc-wrapper-data.txt
/usr/share/openmpi/mpicxx-wrapper-data.txt
/usr/share/openmpi/mpif77-wrapper-data.txt
/usr/share/openmpi/mpif90-wrapper-data.txt
/usr/share/openmpi/mpifort-wrapper-data.txt
/usr/share/openmpi/openmpi-valgrind.supp
/usr/share/openmpi/ortecc-wrapper-data.txt

%files dev
%defattr(-,root,root,-)
/usr/include/mpi-ext.h
/usr/include/mpi.h
/usr/include/mpi_portable_platform.h
/usr/include/mpif-c-constants-decl.h
/usr/include/mpif-config.h
/usr/include/mpif-constants.h
/usr/include/mpif-ext.h
/usr/include/mpif-externals.h
/usr/include/mpif-handles.h
/usr/include/mpif-io-constants.h
/usr/include/mpif-io-handles.h
/usr/include/mpif-sentinels.h
/usr/include/mpif-sizeof.h
/usr/include/mpif.h
/usr/include/openmpi/mpiext/mpiext_affinity_c.h
/usr/include/openmpi/mpiext/mpiext_cuda_c.h
/usr/include/openmpi/mpiext/mpiext_pcollreq_c.h
/usr/include/openmpi/mpiext/mpiext_pcollreq_mpifh.h
/usr/include/openmpi/mpiext/pmpiext_pcollreq_c.h
/usr/lib64/pkgconfig/ompi-c.pc
/usr/lib64/pkgconfig/ompi-cxx.pc
/usr/lib64/pkgconfig/ompi-f77.pc
/usr/lib64/pkgconfig/ompi-f90.pc
/usr/lib64/pkgconfig/ompi-fort.pc
/usr/lib64/pkgconfig/ompi.pc
/usr/lib64/pkgconfig/orte.pc
/usr/share/man/man3/MPI.3
/usr/share/man/man3/MPIX_Allgather_init.3
/usr/share/man/man3/MPIX_Allgatherv_init.3
/usr/share/man/man3/MPIX_Allreduce_init.3
/usr/share/man/man3/MPIX_Alltoall_init.3
/usr/share/man/man3/MPIX_Alltoallv_init.3
/usr/share/man/man3/MPIX_Alltoallw_init.3
/usr/share/man/man3/MPIX_Barrier_init.3
/usr/share/man/man3/MPIX_Bcast_init.3
/usr/share/man/man3/MPIX_Exscan_init.3
/usr/share/man/man3/MPIX_Gather_init.3
/usr/share/man/man3/MPIX_Gatherv_init.3
/usr/share/man/man3/MPIX_Neighbor_allgather_init.3
/usr/share/man/man3/MPIX_Neighbor_allgatherv_init.3
/usr/share/man/man3/MPIX_Neighbor_alltoall_init.3
/usr/share/man/man3/MPIX_Neighbor_alltoallv_init.3
/usr/share/man/man3/MPIX_Neighbor_alltoallw_init.3
/usr/share/man/man3/MPIX_Query_cuda_support.3
/usr/share/man/man3/MPIX_Reduce_init.3
/usr/share/man/man3/MPIX_Reduce_scatter_block_init.3
/usr/share/man/man3/MPIX_Reduce_scatter_init.3
/usr/share/man/man3/MPIX_Scan_init.3
/usr/share/man/man3/MPIX_Scatter_init.3
/usr/share/man/man3/MPIX_Scatterv_init.3
/usr/share/man/man3/MPI_Abort.3
/usr/share/man/man3/MPI_Accumulate.3
/usr/share/man/man3/MPI_Add_error_class.3
/usr/share/man/man3/MPI_Add_error_code.3
/usr/share/man/man3/MPI_Add_error_string.3
/usr/share/man/man3/MPI_Address.3
/usr/share/man/man3/MPI_Aint_add.3
/usr/share/man/man3/MPI_Aint_diff.3
/usr/share/man/man3/MPI_Allgather.3
/usr/share/man/man3/MPI_Allgatherv.3
/usr/share/man/man3/MPI_Alloc_mem.3
/usr/share/man/man3/MPI_Allreduce.3
/usr/share/man/man3/MPI_Alltoall.3
/usr/share/man/man3/MPI_Alltoallv.3
/usr/share/man/man3/MPI_Alltoallw.3
/usr/share/man/man3/MPI_Attr_delete.3
/usr/share/man/man3/MPI_Attr_get.3
/usr/share/man/man3/MPI_Attr_put.3
/usr/share/man/man3/MPI_Barrier.3
/usr/share/man/man3/MPI_Bcast.3
/usr/share/man/man3/MPI_Bsend.3
/usr/share/man/man3/MPI_Bsend_init.3
/usr/share/man/man3/MPI_Buffer_attach.3
/usr/share/man/man3/MPI_Buffer_detach.3
/usr/share/man/man3/MPI_Cancel.3
/usr/share/man/man3/MPI_Cart_coords.3
/usr/share/man/man3/MPI_Cart_create.3
/usr/share/man/man3/MPI_Cart_get.3
/usr/share/man/man3/MPI_Cart_map.3
/usr/share/man/man3/MPI_Cart_rank.3
/usr/share/man/man3/MPI_Cart_shift.3
/usr/share/man/man3/MPI_Cart_sub.3
/usr/share/man/man3/MPI_Cartdim_get.3
/usr/share/man/man3/MPI_Close_port.3
/usr/share/man/man3/MPI_Comm_accept.3
/usr/share/man/man3/MPI_Comm_c2f.3
/usr/share/man/man3/MPI_Comm_call_errhandler.3
/usr/share/man/man3/MPI_Comm_compare.3
/usr/share/man/man3/MPI_Comm_connect.3
/usr/share/man/man3/MPI_Comm_create.3
/usr/share/man/man3/MPI_Comm_create_errhandler.3
/usr/share/man/man3/MPI_Comm_create_group.3
/usr/share/man/man3/MPI_Comm_create_keyval.3
/usr/share/man/man3/MPI_Comm_delete_attr.3
/usr/share/man/man3/MPI_Comm_disconnect.3
/usr/share/man/man3/MPI_Comm_dup.3
/usr/share/man/man3/MPI_Comm_dup_with_info.3
/usr/share/man/man3/MPI_Comm_f2c.3
/usr/share/man/man3/MPI_Comm_free.3
/usr/share/man/man3/MPI_Comm_free_keyval.3
/usr/share/man/man3/MPI_Comm_get_attr.3
/usr/share/man/man3/MPI_Comm_get_errhandler.3
/usr/share/man/man3/MPI_Comm_get_info.3
/usr/share/man/man3/MPI_Comm_get_name.3
/usr/share/man/man3/MPI_Comm_get_parent.3
/usr/share/man/man3/MPI_Comm_group.3
/usr/share/man/man3/MPI_Comm_idup.3
/usr/share/man/man3/MPI_Comm_join.3
/usr/share/man/man3/MPI_Comm_rank.3
/usr/share/man/man3/MPI_Comm_remote_group.3
/usr/share/man/man3/MPI_Comm_remote_size.3
/usr/share/man/man3/MPI_Comm_set_attr.3
/usr/share/man/man3/MPI_Comm_set_errhandler.3
/usr/share/man/man3/MPI_Comm_set_info.3
/usr/share/man/man3/MPI_Comm_set_name.3
/usr/share/man/man3/MPI_Comm_size.3
/usr/share/man/man3/MPI_Comm_spawn.3
/usr/share/man/man3/MPI_Comm_spawn_multiple.3
/usr/share/man/man3/MPI_Comm_split.3
/usr/share/man/man3/MPI_Comm_split_type.3
/usr/share/man/man3/MPI_Comm_test_inter.3
/usr/share/man/man3/MPI_Compare_and_swap.3
/usr/share/man/man3/MPI_Dims_create.3
/usr/share/man/man3/MPI_Dist_graph_create.3
/usr/share/man/man3/MPI_Dist_graph_create_adjacent.3
/usr/share/man/man3/MPI_Dist_graph_neighbors.3
/usr/share/man/man3/MPI_Dist_graph_neighbors_count.3
/usr/share/man/man3/MPI_Errhandler_create.3
/usr/share/man/man3/MPI_Errhandler_free.3
/usr/share/man/man3/MPI_Errhandler_get.3
/usr/share/man/man3/MPI_Errhandler_set.3
/usr/share/man/man3/MPI_Error_class.3
/usr/share/man/man3/MPI_Error_string.3
/usr/share/man/man3/MPI_Exscan.3
/usr/share/man/man3/MPI_Fetch_and_op.3
/usr/share/man/man3/MPI_File_c2f.3
/usr/share/man/man3/MPI_File_call_errhandler.3
/usr/share/man/man3/MPI_File_close.3
/usr/share/man/man3/MPI_File_create_errhandler.3
/usr/share/man/man3/MPI_File_delete.3
/usr/share/man/man3/MPI_File_f2c.3
/usr/share/man/man3/MPI_File_get_amode.3
/usr/share/man/man3/MPI_File_get_atomicity.3
/usr/share/man/man3/MPI_File_get_byte_offset.3
/usr/share/man/man3/MPI_File_get_errhandler.3
/usr/share/man/man3/MPI_File_get_group.3
/usr/share/man/man3/MPI_File_get_info.3
/usr/share/man/man3/MPI_File_get_position.3
/usr/share/man/man3/MPI_File_get_position_shared.3
/usr/share/man/man3/MPI_File_get_size.3
/usr/share/man/man3/MPI_File_get_type_extent.3
/usr/share/man/man3/MPI_File_get_view.3
/usr/share/man/man3/MPI_File_iread.3
/usr/share/man/man3/MPI_File_iread_all.3
/usr/share/man/man3/MPI_File_iread_at.3
/usr/share/man/man3/MPI_File_iread_at_all.3
/usr/share/man/man3/MPI_File_iread_shared.3
/usr/share/man/man3/MPI_File_iwrite.3
/usr/share/man/man3/MPI_File_iwrite_all.3
/usr/share/man/man3/MPI_File_iwrite_at.3
/usr/share/man/man3/MPI_File_iwrite_at_all.3
/usr/share/man/man3/MPI_File_iwrite_shared.3
/usr/share/man/man3/MPI_File_open.3
/usr/share/man/man3/MPI_File_preallocate.3
/usr/share/man/man3/MPI_File_read.3
/usr/share/man/man3/MPI_File_read_all.3
/usr/share/man/man3/MPI_File_read_all_begin.3
/usr/share/man/man3/MPI_File_read_all_end.3
/usr/share/man/man3/MPI_File_read_at.3
/usr/share/man/man3/MPI_File_read_at_all.3
/usr/share/man/man3/MPI_File_read_at_all_begin.3
/usr/share/man/man3/MPI_File_read_at_all_end.3
/usr/share/man/man3/MPI_File_read_ordered.3
/usr/share/man/man3/MPI_File_read_ordered_begin.3
/usr/share/man/man3/MPI_File_read_ordered_end.3
/usr/share/man/man3/MPI_File_read_shared.3
/usr/share/man/man3/MPI_File_seek.3
/usr/share/man/man3/MPI_File_seek_shared.3
/usr/share/man/man3/MPI_File_set_atomicity.3
/usr/share/man/man3/MPI_File_set_errhandler.3
/usr/share/man/man3/MPI_File_set_info.3
/usr/share/man/man3/MPI_File_set_size.3
/usr/share/man/man3/MPI_File_set_view.3
/usr/share/man/man3/MPI_File_sync.3
/usr/share/man/man3/MPI_File_write.3
/usr/share/man/man3/MPI_File_write_all.3
/usr/share/man/man3/MPI_File_write_all_begin.3
/usr/share/man/man3/MPI_File_write_all_end.3
/usr/share/man/man3/MPI_File_write_at.3
/usr/share/man/man3/MPI_File_write_at_all.3
/usr/share/man/man3/MPI_File_write_at_all_begin.3
/usr/share/man/man3/MPI_File_write_at_all_end.3
/usr/share/man/man3/MPI_File_write_ordered.3
/usr/share/man/man3/MPI_File_write_ordered_begin.3
/usr/share/man/man3/MPI_File_write_ordered_end.3
/usr/share/man/man3/MPI_File_write_shared.3
/usr/share/man/man3/MPI_Finalize.3
/usr/share/man/man3/MPI_Finalized.3
/usr/share/man/man3/MPI_Free_mem.3
/usr/share/man/man3/MPI_Gather.3
/usr/share/man/man3/MPI_Gatherv.3
/usr/share/man/man3/MPI_Get.3
/usr/share/man/man3/MPI_Get_accumulate.3
/usr/share/man/man3/MPI_Get_address.3
/usr/share/man/man3/MPI_Get_count.3
/usr/share/man/man3/MPI_Get_elements.3
/usr/share/man/man3/MPI_Get_elements_x.3
/usr/share/man/man3/MPI_Get_library_version.3
/usr/share/man/man3/MPI_Get_processor_name.3
/usr/share/man/man3/MPI_Get_version.3
/usr/share/man/man3/MPI_Graph_create.3
/usr/share/man/man3/MPI_Graph_get.3
/usr/share/man/man3/MPI_Graph_map.3
/usr/share/man/man3/MPI_Graph_neighbors.3
/usr/share/man/man3/MPI_Graph_neighbors_count.3
/usr/share/man/man3/MPI_Graphdims_get.3
/usr/share/man/man3/MPI_Grequest_complete.3
/usr/share/man/man3/MPI_Grequest_start.3
/usr/share/man/man3/MPI_Group_c2f.3
/usr/share/man/man3/MPI_Group_compare.3
/usr/share/man/man3/MPI_Group_difference.3
/usr/share/man/man3/MPI_Group_excl.3
/usr/share/man/man3/MPI_Group_f2c.3
/usr/share/man/man3/MPI_Group_free.3
/usr/share/man/man3/MPI_Group_incl.3
/usr/share/man/man3/MPI_Group_intersection.3
/usr/share/man/man3/MPI_Group_range_excl.3
/usr/share/man/man3/MPI_Group_range_incl.3
/usr/share/man/man3/MPI_Group_rank.3
/usr/share/man/man3/MPI_Group_size.3
/usr/share/man/man3/MPI_Group_translate_ranks.3
/usr/share/man/man3/MPI_Group_union.3
/usr/share/man/man3/MPI_Iallgather.3
/usr/share/man/man3/MPI_Iallgatherv.3
/usr/share/man/man3/MPI_Iallreduce.3
/usr/share/man/man3/MPI_Ialltoall.3
/usr/share/man/man3/MPI_Ialltoallv.3
/usr/share/man/man3/MPI_Ialltoallw.3
/usr/share/man/man3/MPI_Ibarrier.3
/usr/share/man/man3/MPI_Ibcast.3
/usr/share/man/man3/MPI_Ibsend.3
/usr/share/man/man3/MPI_Iexscan.3
/usr/share/man/man3/MPI_Igather.3
/usr/share/man/man3/MPI_Igatherv.3
/usr/share/man/man3/MPI_Improbe.3
/usr/share/man/man3/MPI_Imrecv.3
/usr/share/man/man3/MPI_Ineighbor_allgather.3
/usr/share/man/man3/MPI_Ineighbor_allgatherv.3
/usr/share/man/man3/MPI_Ineighbor_alltoall.3
/usr/share/man/man3/MPI_Ineighbor_alltoallv.3
/usr/share/man/man3/MPI_Ineighbor_alltoallw.3
/usr/share/man/man3/MPI_Info_c2f.3
/usr/share/man/man3/MPI_Info_create.3
/usr/share/man/man3/MPI_Info_delete.3
/usr/share/man/man3/MPI_Info_dup.3
/usr/share/man/man3/MPI_Info_env.3
/usr/share/man/man3/MPI_Info_f2c.3
/usr/share/man/man3/MPI_Info_free.3
/usr/share/man/man3/MPI_Info_get.3
/usr/share/man/man3/MPI_Info_get_nkeys.3
/usr/share/man/man3/MPI_Info_get_nthkey.3
/usr/share/man/man3/MPI_Info_get_valuelen.3
/usr/share/man/man3/MPI_Info_set.3
/usr/share/man/man3/MPI_Init.3
/usr/share/man/man3/MPI_Init_thread.3
/usr/share/man/man3/MPI_Initialized.3
/usr/share/man/man3/MPI_Intercomm_create.3
/usr/share/man/man3/MPI_Intercomm_merge.3
/usr/share/man/man3/MPI_Iprobe.3
/usr/share/man/man3/MPI_Irecv.3
/usr/share/man/man3/MPI_Ireduce.3
/usr/share/man/man3/MPI_Ireduce_scatter.3
/usr/share/man/man3/MPI_Ireduce_scatter_block.3
/usr/share/man/man3/MPI_Irsend.3
/usr/share/man/man3/MPI_Is_thread_main.3
/usr/share/man/man3/MPI_Iscan.3
/usr/share/man/man3/MPI_Iscatter.3
/usr/share/man/man3/MPI_Iscatterv.3
/usr/share/man/man3/MPI_Isend.3
/usr/share/man/man3/MPI_Issend.3
/usr/share/man/man3/MPI_Keyval_create.3
/usr/share/man/man3/MPI_Keyval_free.3
/usr/share/man/man3/MPI_Lookup_name.3
/usr/share/man/man3/MPI_Message_c2f.3
/usr/share/man/man3/MPI_Message_f2c.3
/usr/share/man/man3/MPI_Mprobe.3
/usr/share/man/man3/MPI_Mrecv.3
/usr/share/man/man3/MPI_Neighbor_allgather.3
/usr/share/man/man3/MPI_Neighbor_allgatherv.3
/usr/share/man/man3/MPI_Neighbor_alltoall.3
/usr/share/man/man3/MPI_Neighbor_alltoallv.3
/usr/share/man/man3/MPI_Neighbor_alltoallw.3
/usr/share/man/man3/MPI_Op_c2f.3
/usr/share/man/man3/MPI_Op_commutative.3
/usr/share/man/man3/MPI_Op_create.3
/usr/share/man/man3/MPI_Op_f2c.3
/usr/share/man/man3/MPI_Op_free.3
/usr/share/man/man3/MPI_Open_port.3
/usr/share/man/man3/MPI_Pack.3
/usr/share/man/man3/MPI_Pack_external.3
/usr/share/man/man3/MPI_Pack_external_size.3
/usr/share/man/man3/MPI_Pack_size.3
/usr/share/man/man3/MPI_Pcontrol.3
/usr/share/man/man3/MPI_Probe.3
/usr/share/man/man3/MPI_Publish_name.3
/usr/share/man/man3/MPI_Put.3
/usr/share/man/man3/MPI_Query_thread.3
/usr/share/man/man3/MPI_Raccumulate.3
/usr/share/man/man3/MPI_Recv.3
/usr/share/man/man3/MPI_Recv_init.3
/usr/share/man/man3/MPI_Reduce.3
/usr/share/man/man3/MPI_Reduce_local.3
/usr/share/man/man3/MPI_Reduce_scatter.3
/usr/share/man/man3/MPI_Reduce_scatter_block.3
/usr/share/man/man3/MPI_Register_datarep.3
/usr/share/man/man3/MPI_Request_c2f.3
/usr/share/man/man3/MPI_Request_f2c.3
/usr/share/man/man3/MPI_Request_free.3
/usr/share/man/man3/MPI_Request_get_status.3
/usr/share/man/man3/MPI_Rget.3
/usr/share/man/man3/MPI_Rget_accumulate.3
/usr/share/man/man3/MPI_Rput.3
/usr/share/man/man3/MPI_Rsend.3
/usr/share/man/man3/MPI_Rsend_init.3
/usr/share/man/man3/MPI_Scan.3
/usr/share/man/man3/MPI_Scatter.3
/usr/share/man/man3/MPI_Scatterv.3
/usr/share/man/man3/MPI_Send.3
/usr/share/man/man3/MPI_Send_init.3
/usr/share/man/man3/MPI_Sendrecv.3
/usr/share/man/man3/MPI_Sendrecv_replace.3
/usr/share/man/man3/MPI_Sizeof.3
/usr/share/man/man3/MPI_Ssend.3
/usr/share/man/man3/MPI_Ssend_init.3
/usr/share/man/man3/MPI_Start.3
/usr/share/man/man3/MPI_Startall.3
/usr/share/man/man3/MPI_Status_c2f.3
/usr/share/man/man3/MPI_Status_f2c.3
/usr/share/man/man3/MPI_Status_set_cancelled.3
/usr/share/man/man3/MPI_Status_set_elements.3
/usr/share/man/man3/MPI_Status_set_elements_x.3
/usr/share/man/man3/MPI_T_category_changed.3
/usr/share/man/man3/MPI_T_category_get_categories.3
/usr/share/man/man3/MPI_T_category_get_cvars.3
/usr/share/man/man3/MPI_T_category_get_info.3
/usr/share/man/man3/MPI_T_category_get_num.3
/usr/share/man/man3/MPI_T_category_get_pvars.3
/usr/share/man/man3/MPI_T_cvar_get_info.3
/usr/share/man/man3/MPI_T_cvar_get_num.3
/usr/share/man/man3/MPI_T_cvar_handle_alloc.3
/usr/share/man/man3/MPI_T_cvar_handle_free.3
/usr/share/man/man3/MPI_T_cvar_read.3
/usr/share/man/man3/MPI_T_cvar_write.3
/usr/share/man/man3/MPI_T_enum_get_info.3
/usr/share/man/man3/MPI_T_enum_get_item.3
/usr/share/man/man3/MPI_T_finalize.3
/usr/share/man/man3/MPI_T_init_thread.3
/usr/share/man/man3/MPI_T_pvar_get_info.3
/usr/share/man/man3/MPI_T_pvar_get_num.3
/usr/share/man/man3/MPI_T_pvar_handle_alloc.3
/usr/share/man/man3/MPI_T_pvar_handle_free.3
/usr/share/man/man3/MPI_T_pvar_read.3
/usr/share/man/man3/MPI_T_pvar_readreset.3
/usr/share/man/man3/MPI_T_pvar_reset.3
/usr/share/man/man3/MPI_T_pvar_session_create.3
/usr/share/man/man3/MPI_T_pvar_session_free.3
/usr/share/man/man3/MPI_T_pvar_start.3
/usr/share/man/man3/MPI_T_pvar_stop.3
/usr/share/man/man3/MPI_T_pvar_write.3
/usr/share/man/man3/MPI_Test.3
/usr/share/man/man3/MPI_Test_cancelled.3
/usr/share/man/man3/MPI_Testall.3
/usr/share/man/man3/MPI_Testany.3
/usr/share/man/man3/MPI_Testsome.3
/usr/share/man/man3/MPI_Topo_test.3
/usr/share/man/man3/MPI_Type_c2f.3
/usr/share/man/man3/MPI_Type_commit.3
/usr/share/man/man3/MPI_Type_contiguous.3
/usr/share/man/man3/MPI_Type_create_darray.3
/usr/share/man/man3/MPI_Type_create_f90_complex.3
/usr/share/man/man3/MPI_Type_create_f90_integer.3
/usr/share/man/man3/MPI_Type_create_f90_real.3
/usr/share/man/man3/MPI_Type_create_hindexed.3
/usr/share/man/man3/MPI_Type_create_hindexed_block.3
/usr/share/man/man3/MPI_Type_create_hvector.3
/usr/share/man/man3/MPI_Type_create_indexed_block.3
/usr/share/man/man3/MPI_Type_create_keyval.3
/usr/share/man/man3/MPI_Type_create_resized.3
/usr/share/man/man3/MPI_Type_create_struct.3
/usr/share/man/man3/MPI_Type_create_subarray.3
/usr/share/man/man3/MPI_Type_delete_attr.3
/usr/share/man/man3/MPI_Type_dup.3
/usr/share/man/man3/MPI_Type_extent.3
/usr/share/man/man3/MPI_Type_f2c.3
/usr/share/man/man3/MPI_Type_free.3
/usr/share/man/man3/MPI_Type_free_keyval.3
/usr/share/man/man3/MPI_Type_get_attr.3
/usr/share/man/man3/MPI_Type_get_contents.3
/usr/share/man/man3/MPI_Type_get_envelope.3
/usr/share/man/man3/MPI_Type_get_extent.3
/usr/share/man/man3/MPI_Type_get_extent_x.3
/usr/share/man/man3/MPI_Type_get_name.3
/usr/share/man/man3/MPI_Type_get_true_extent.3
/usr/share/man/man3/MPI_Type_get_true_extent_x.3
/usr/share/man/man3/MPI_Type_hindexed.3
/usr/share/man/man3/MPI_Type_hvector.3
/usr/share/man/man3/MPI_Type_indexed.3
/usr/share/man/man3/MPI_Type_lb.3
/usr/share/man/man3/MPI_Type_match_size.3
/usr/share/man/man3/MPI_Type_set_attr.3
/usr/share/man/man3/MPI_Type_set_name.3
/usr/share/man/man3/MPI_Type_size.3
/usr/share/man/man3/MPI_Type_size_x.3
/usr/share/man/man3/MPI_Type_struct.3
/usr/share/man/man3/MPI_Type_ub.3
/usr/share/man/man3/MPI_Type_vector.3
/usr/share/man/man3/MPI_Unpack.3
/usr/share/man/man3/MPI_Unpack_external.3
/usr/share/man/man3/MPI_Unpublish_name.3
/usr/share/man/man3/MPI_Wait.3
/usr/share/man/man3/MPI_Waitall.3
/usr/share/man/man3/MPI_Waitany.3
/usr/share/man/man3/MPI_Waitsome.3
/usr/share/man/man3/MPI_Win_allocate.3
/usr/share/man/man3/MPI_Win_allocate_shared.3
/usr/share/man/man3/MPI_Win_attach.3
/usr/share/man/man3/MPI_Win_c2f.3
/usr/share/man/man3/MPI_Win_call_errhandler.3
/usr/share/man/man3/MPI_Win_complete.3
/usr/share/man/man3/MPI_Win_create.3
/usr/share/man/man3/MPI_Win_create_dynamic.3
/usr/share/man/man3/MPI_Win_create_errhandler.3
/usr/share/man/man3/MPI_Win_create_keyval.3
/usr/share/man/man3/MPI_Win_delete_attr.3
/usr/share/man/man3/MPI_Win_detach.3
/usr/share/man/man3/MPI_Win_f2c.3
/usr/share/man/man3/MPI_Win_fence.3
/usr/share/man/man3/MPI_Win_flush.3
/usr/share/man/man3/MPI_Win_flush_all.3
/usr/share/man/man3/MPI_Win_flush_local.3
/usr/share/man/man3/MPI_Win_flush_local_all.3
/usr/share/man/man3/MPI_Win_free.3
/usr/share/man/man3/MPI_Win_free_keyval.3
/usr/share/man/man3/MPI_Win_get_attr.3
/usr/share/man/man3/MPI_Win_get_errhandler.3
/usr/share/man/man3/MPI_Win_get_group.3
/usr/share/man/man3/MPI_Win_get_info.3
/usr/share/man/man3/MPI_Win_get_name.3
/usr/share/man/man3/MPI_Win_lock.3
/usr/share/man/man3/MPI_Win_lock_all.3
/usr/share/man/man3/MPI_Win_post.3
/usr/share/man/man3/MPI_Win_set_attr.3
/usr/share/man/man3/MPI_Win_set_errhandler.3
/usr/share/man/man3/MPI_Win_set_info.3
/usr/share/man/man3/MPI_Win_set_name.3
/usr/share/man/man3/MPI_Win_shared_query.3
/usr/share/man/man3/MPI_Win_start.3
/usr/share/man/man3/MPI_Win_sync.3
/usr/share/man/man3/MPI_Win_test.3
/usr/share/man/man3/MPI_Win_unlock.3
/usr/share/man/man3/MPI_Win_unlock_all.3
/usr/share/man/man3/MPI_Win_wait.3
/usr/share/man/man3/MPI_Wtick.3
/usr/share/man/man3/MPI_Wtime.3
/usr/share/man/man3/OMPI_Affinity_str.3
/usr/share/man/man3/OpenMPI.3

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-openmpi

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmca_common_monitoring.so
/usr/lib64/libmca_common_monitoring.so.50
/usr/lib64/libmca_common_monitoring.so.50.20.0
/usr/lib64/libmca_common_ompio.so
/usr/lib64/libmca_common_ompio.so.41
/usr/lib64/libmca_common_ompio.so.41.29.3
/usr/lib64/libmca_common_sm.so
/usr/lib64/libmca_common_sm.so.40
/usr/lib64/libmca_common_sm.so.40.30.0
/usr/lib64/libmpi.so
/usr/lib64/libmpi.so.40
/usr/lib64/libmpi.so.40.30.3
/usr/lib64/libmpi_mpifh.so
/usr/lib64/libmpi_mpifh.so.40
/usr/lib64/libmpi_mpifh.so.40.30.0
/usr/lib64/libmpi_usempi_ignore_tkr.so
/usr/lib64/libmpi_usempi_ignore_tkr.so.40
/usr/lib64/libmpi_usempi_ignore_tkr.so.40.30.0
/usr/lib64/libmpi_usempif08.so
/usr/lib64/libmpi_usempif08.so.40
/usr/lib64/libmpi_usempif08.so.40.30.0
/usr/lib64/libompitrace.so
/usr/lib64/libompitrace.so.40
/usr/lib64/libompitrace.so.40.30.1
/usr/lib64/libopen-pal.so
/usr/lib64/libopen-pal.so.40
/usr/lib64/libopen-pal.so.40.30.2
/usr/lib64/libopen-rte.so
/usr/lib64/libopen-rte.so.40
/usr/lib64/libopen-rte.so.40.30.2
/usr/lib64/ompi_monitoring_prof.so
/usr/lib64/openmpi/libompi_dbg_msgq.so
/usr/lib64/openmpi/mca_allocator_basic.so
/usr/lib64/openmpi/mca_allocator_bucket.so
/usr/lib64/openmpi/mca_bml_r2.so
/usr/lib64/openmpi/mca_btl_self.so
/usr/lib64/openmpi/mca_btl_sm.so
/usr/lib64/openmpi/mca_btl_tcp.so
/usr/lib64/openmpi/mca_btl_vader.so
/usr/lib64/openmpi/mca_coll_adapt.so
/usr/lib64/openmpi/mca_coll_basic.so
/usr/lib64/openmpi/mca_coll_han.so
/usr/lib64/openmpi/mca_coll_inter.so
/usr/lib64/openmpi/mca_coll_libnbc.so
/usr/lib64/openmpi/mca_coll_monitoring.so
/usr/lib64/openmpi/mca_coll_self.so
/usr/lib64/openmpi/mca_coll_sm.so
/usr/lib64/openmpi/mca_coll_sync.so
/usr/lib64/openmpi/mca_coll_tuned.so
/usr/lib64/openmpi/mca_compress_bzip.so
/usr/lib64/openmpi/mca_compress_gzip.so
/usr/lib64/openmpi/mca_crs_none.so
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
/usr/lib64/openmpi/mca_fcoll_two_phase.so
/usr/lib64/openmpi/mca_fcoll_vulcan.so
/usr/lib64/openmpi/mca_filem_raw.so
/usr/lib64/openmpi/mca_fs_ufs.so
/usr/lib64/openmpi/mca_grpcomm_direct.so
/usr/lib64/openmpi/mca_io_ompio.so
/usr/lib64/openmpi/mca_io_romio321.so
/usr/lib64/openmpi/mca_iof_hnp.so
/usr/lib64/openmpi/mca_iof_orted.so
/usr/lib64/openmpi/mca_iof_tool.so
/usr/lib64/openmpi/mca_mpool_hugepage.so
/usr/lib64/openmpi/mca_odls_default.so
/usr/lib64/openmpi/mca_odls_pspawn.so
/usr/lib64/openmpi/mca_oob_tcp.so
/usr/lib64/openmpi/mca_op_avx.so
/usr/lib64/openmpi/mca_osc_monitoring.so
/usr/lib64/openmpi/mca_osc_pt2pt.so
/usr/lib64/openmpi/mca_osc_rdma.so
/usr/lib64/openmpi/mca_osc_sm.so
/usr/lib64/openmpi/mca_patcher_overwrite.so
/usr/lib64/openmpi/mca_plm_isolated.so
/usr/lib64/openmpi/mca_plm_rsh.so
/usr/lib64/openmpi/mca_plm_slurm.so
/usr/lib64/openmpi/mca_pmix_ext3x.so
/usr/lib64/openmpi/mca_pmix_flux.so
/usr/lib64/openmpi/mca_pmix_isolated.so
/usr/lib64/openmpi/mca_pml_cm.so
/usr/lib64/openmpi/mca_pml_monitoring.so
/usr/lib64/openmpi/mca_pml_ob1.so
/usr/lib64/openmpi/mca_pstat_linux.so
/usr/lib64/openmpi/mca_ras_simulator.so
/usr/lib64/openmpi/mca_ras_slurm.so
/usr/lib64/openmpi/mca_rcache_grdma.so
/usr/lib64/openmpi/mca_reachable_weighted.so
/usr/lib64/openmpi/mca_regx_fwd.so
/usr/lib64/openmpi/mca_regx_naive.so
/usr/lib64/openmpi/mca_regx_reverse.so
/usr/lib64/openmpi/mca_rmaps_mindist.so
/usr/lib64/openmpi/mca_rmaps_ppr.so
/usr/lib64/openmpi/mca_rmaps_rank_file.so
/usr/lib64/openmpi/mca_rmaps_resilient.so
/usr/lib64/openmpi/mca_rmaps_round_robin.so
/usr/lib64/openmpi/mca_rmaps_seq.so
/usr/lib64/openmpi/mca_rml_oob.so
/usr/lib64/openmpi/mca_routed_binomial.so
/usr/lib64/openmpi/mca_routed_direct.so
/usr/lib64/openmpi/mca_routed_radix.so
/usr/lib64/openmpi/mca_rtc_hwloc.so
/usr/lib64/openmpi/mca_schizo_flux.so
/usr/lib64/openmpi/mca_schizo_jsm.so
/usr/lib64/openmpi/mca_schizo_ompi.so
/usr/lib64/openmpi/mca_schizo_orte.so
/usr/lib64/openmpi/mca_schizo_slurm.so
/usr/lib64/openmpi/mca_sharedfp_individual.so
/usr/lib64/openmpi/mca_sharedfp_lockedfile.so
/usr/lib64/openmpi/mca_sharedfp_sm.so
/usr/lib64/openmpi/mca_shmem_mmap.so
/usr/lib64/openmpi/mca_shmem_posix.so
/usr/lib64/openmpi/mca_shmem_sysv.so
/usr/lib64/openmpi/mca_state_app.so
/usr/lib64/openmpi/mca_state_hnp.so
/usr/lib64/openmpi/mca_state_novm.so
/usr/lib64/openmpi/mca_state_orted.so
/usr/lib64/openmpi/mca_state_tool.so
/usr/lib64/openmpi/mca_topo_basic.so
/usr/lib64/openmpi/mca_topo_treematch.so
/usr/lib64/openmpi/mca_vprotocol_pessimist.so
/usr/share/clear/optimized-elf/lib*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/openmpi/1d219195f5b198de4d80822b54ee0511f0d38361
/usr/share/package-licenses/openmpi/23ae9dd3b06c170d1abfbdf517a2e4fea90b7cdd
/usr/share/package-licenses/openmpi/2530bd3ed2c1661445dacd664b277d1f092c56f3
/usr/share/package-licenses/openmpi/458149cf961c544a997c5de2d3df83cab6e2c08c
/usr/share/package-licenses/openmpi/80be8a39adf3f4419e3f7153aba2ae318eeec910
/usr/share/package-licenses/openmpi/c0fb365dcaaae482fe7c3673c97d0e8c6d21636d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mpiCC.1
/usr/share/man/man1/mpic++.1
/usr/share/man/man1/mpicc.1
/usr/share/man/man1/mpicxx.1
/usr/share/man/man1/mpiexec.1
/usr/share/man/man1/mpif77.1
/usr/share/man/man1/mpif90.1
/usr/share/man/man1/mpifort.1
/usr/share/man/man1/mpirun.1
/usr/share/man/man1/ompi-clean.1
/usr/share/man/man1/ompi-server.1
/usr/share/man/man1/ompi_info.1
/usr/share/man/man1/opal_wrapper.1
/usr/share/man/man1/orte-clean.1
/usr/share/man/man1/orte-info.1
/usr/share/man/man1/orte-server.1
/usr/share/man/man1/orted.1
/usr/share/man/man1/orterun.1
/usr/share/man/man7/ompi_crcp.7
/usr/share/man/man7/opal_crs.7
/usr/share/man/man7/orte_filem.7
/usr/share/man/man7/orte_hosts.7
/usr/share/man/man7/orte_snapc.7
/usr/share/man/man7/orte_sstore.7

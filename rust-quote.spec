# Rust packages always list license files and docs
# inside the crate as well as the containing directory
%undefine _duplicate_files_terminate_build
# Avoid dependencies
%bcond_with check
%global debug_package %{nil}

%global crate quote

Name:           rust-quote
Version:        1.0.33
Release:        1
Summary:        Quasi-quoting macro quote!(...)
Group:          Development/Rust

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/quote
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  (crate(proc-macro2) >= 1.0.66 with crate(proc-macro2) < 2.0.0~)
BuildRequires:  (crate(proc-macro2/proc-macro) >= 1.0.66 with crate(proc-macro2/proc-macro) < 2.0.0~)
BuildRequires:  rust >= 1.56
%if %{with check}
BuildRequires:  (crate(rustversion/default) >= 1.0.0 with crate(rustversion/default) < 2.0.0~)
BuildRequires:  (crate(trybuild/default) >= 1.0.66 with crate(trybuild/default) < 2.0.0~)
BuildRequires:  (crate(trybuild/diff) >= 1.0.66 with crate(trybuild/diff) < 2.0.0~)
%endif

%global _description %{expand:
Quasi-quoting macro quote!(...).}

%description %{_description}

%package        devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(quote) = 1.0.33
Requires:       (crate(proc-macro2) >= 1.0.66 with crate(proc-macro2) < 2.0.0~)
Requires:       cargo
Requires:       rust >= 1.56

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(quote/default) = 1.0.33
Requires:       cargo
Requires:       crate(quote) = 1.0.33
Requires:       crate(quote/proc-macro) = 1.0.33

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+proc-macro-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(quote/proc-macro) = 1.0.33
Requires:       (crate(proc-macro2/proc-macro) >= 1.0.66 with crate(proc-macro2/proc-macro) < 2.0.0~)
Requires:       cargo
Requires:       crate(quote) = 1.0.33

%description -n %{name}+proc-macro-devel %{_description}

This package contains library source intended for building other packages which
use the "proc-macro" feature of the "%{crate}" crate.

%files       -n %{name}+proc-macro-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

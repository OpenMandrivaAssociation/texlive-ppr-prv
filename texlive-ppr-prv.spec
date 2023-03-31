Name:		texlive-ppr-prv
Version:	15878
Release:	2
Summary:	Prosper preview
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ppr-prv
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ppr-prv.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ppr-prv.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ppr-prv.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This class is used with LaTeX presentations using the prosper
class. ppr-prv stands for 'Prosper Preview'. The aim of this
class is to produce a printable version of the slides written
with Prosper, with two slides per page.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ppr-prv/HAP-ppr-prv.def
%{_texmfdistdir}/tex/latex/ppr-prv/ppr-prv.cls
%doc %{_texmfdistdir}/doc/latex/ppr-prv/README
%doc %{_texmfdistdir}/doc/latex/ppr-prv/ppr-prv.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ppr-prv/ppr-prv.dtx
%doc %{_texmfdistdir}/source/latex/ppr-prv/ppr-prv.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

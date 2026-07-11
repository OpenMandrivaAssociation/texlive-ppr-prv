%global tl_name ppr-prv
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.13c
Release:	%{tl_revision}.1
Summary:	Prosper preview
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ppr-prv
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ppr-prv.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ppr-prv.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ppr-prv.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This class is used with LaTeX presentations using the prosper class.
ppr-prv stands for 'Prosper Preview'. The aim of this class is to
produce a printable version of the slides written with Prosper, with two
slides per page.


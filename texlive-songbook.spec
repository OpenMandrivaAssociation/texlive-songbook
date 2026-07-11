%global tl_name songbook
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.5
Release:	%{tl_revision}.1
Summary:	Package for typesetting song lyrics and chord books
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/songbook
License:	lgpl2.1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/songbook.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/songbook.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/songbook.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides an all purpose songbook style. Three types of
output may be created from a single input file: "words and chords" books
for the musicians to play from, "words only" songbooks for the
congregation to sing from, and overhead transparency masters for
congregational use. The package will also print a table of contents, an
index sorted by title and first line, and an index sorted by key, or by
artist/composer. The package attempts to handle songs in multiple keys,
as well as songs in multiple languages.


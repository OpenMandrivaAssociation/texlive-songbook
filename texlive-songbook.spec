Name:		texlive-songbook
Version:	18136
Release:	2
Summary:	Package for typesetting song lyrics and chord books
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/songbook
License:	LGPL2.1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/songbook.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/songbook.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/songbook.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides an all purpose songbook style. Three types
of output may be created from a single input file: "words and
chords" books for the musicians to play from, "words only"
songbooks for the congregation to sing from, and overhead
transparency masters for congregational use. The package will
also print a table of contents, an index sorted by title and
first line, and an index sorted by key, or by artist/composer.
The package attempts to handle songs in multiple keys, as well
as songs in multiple languages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/makeindex/songbook/songbook.ist
%{_texmfdistdir}/tex/latex/songbook/conditionals.sty
%{_texmfdistdir}/tex/latex/songbook/songbook.sty
%doc %{_texmfdistdir}/doc/latex/songbook/LesserGPL.txt
%doc %{_texmfdistdir}/doc/latex/songbook/README
%doc %{_texmfdistdir}/doc/latex/songbook/contrib/CarolBook/CarolBook.tex
%doc %{_texmfdistdir}/doc/latex/songbook/contrib/CarolBook/CarolBookOH.pdf
%doc %{_texmfdistdir}/doc/latex/songbook/contrib/CarolBook/CarolBookWB.pdf
%doc %{_texmfdistdir}/doc/latex/songbook/contrib/README
%doc %{_texmfdistdir}/doc/latex/songbook/contrib/crd2sb/NothingButTheBlood.crd
%doc %{_texmfdistdir}/doc/latex/songbook/contrib/crd2sb/crd2sb
%doc %{_texmfdistdir}/doc/latex/songbook/contrib/crd2sb/crd2sb.txt
%doc %{_texmfdistdir}/doc/latex/songbook/contrib/modulate
%doc %{_texmfdistdir}/doc/latex/songbook/contrib/texchord.sty
%doc %{_texmfdistdir}/doc/latex/songbook/install.txt
%doc %{_texmfdistdir}/doc/latex/songbook/mksbadx
%doc %{_texmfdistdir}/doc/latex/songbook/mksbkdx
%doc %{_texmfdistdir}/doc/latex/songbook/mksbtdx
%doc %{_texmfdistdir}/doc/latex/songbook/sample-sb.tex
%doc %{_texmfdistdir}/doc/latex/songbook/sampleAdx.pdf
%doc %{_texmfdistdir}/doc/latex/songbook/sampleAdx.tex
%doc %{_texmfdistdir}/doc/latex/songbook/sampleCBK.pdf
%doc %{_texmfdistdir}/doc/latex/songbook/sampleCSBK.pdf
%doc %{_texmfdistdir}/doc/latex/songbook/sampleKdx.pdf
%doc %{_texmfdistdir}/doc/latex/songbook/sampleKdx.tex
%doc %{_texmfdistdir}/doc/latex/songbook/sampleOH.pdf
%doc %{_texmfdistdir}/doc/latex/songbook/sampleTdx.pdf
%doc %{_texmfdistdir}/doc/latex/songbook/sampleTdx.tex
%doc %{_texmfdistdir}/doc/latex/songbook/sampleToc.pdf
%doc %{_texmfdistdir}/doc/latex/songbook/sampleToc.tex
%doc %{_texmfdistdir}/doc/latex/songbook/sampleWBK.pdf
%doc %{_texmfdistdir}/doc/latex/songbook/songbook.pdf
#- source
%doc %{_texmfdistdir}/source/latex/songbook/songbook.dtx
%doc %{_texmfdistdir}/source/latex/songbook/songbook.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc source %{buildroot}%{_texmfdistdir}

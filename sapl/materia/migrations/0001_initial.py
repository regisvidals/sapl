# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-25 11:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import sapl.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('comissoes', '0001_initial'),
        ('compilacao', '0001_initial'),
        ('parlamentares', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcompanhamentoMateria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
                ('data_cadastro', models.DateField(auto_now_add=True)),
                ('hash', models.CharField(max_length=8)),
                ('confirmado', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Acompanhamento de Matéria',
                'verbose_name_plural': 'Acompanhamentos de Matéria',
            },
        ),
        migrations.CreateModel(
            name='Anexada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_anexacao', models.DateField(verbose_name='Data Anexação')),
                ('data_desanexacao', models.DateField(blank=True, null=True, verbose_name='Data Desanexação')),
            ],
            options={
                'verbose_name': 'Anexada',
                'verbose_name_plural': 'Anexadas',
            },
        ),
        migrations.CreateModel(
            name='AssuntoMateria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.CharField(max_length=200)),
                ('dispositivo', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Assunto de Matéria',
                'verbose_name_plural': 'Assuntos de Matéria',
            },
        ),
        migrations.CreateModel(
            name='Autoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_autor', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=False, verbose_name='Primeiro Autor')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.Autor', verbose_name='Autor')),
            ],
            options={
                'verbose_name': 'Autoria',
                'verbose_name_plural': 'Autorias',
            },
        ),
        migrations.CreateModel(
            name='DespachoInicial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comissao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='comissoes.Comissao')),
            ],
            options={
                'verbose_name': 'Despacho Inicial',
                'verbose_name_plural': 'Despachos Iniciais',
            },
        ),
        migrations.CreateModel(
            name='DocumentoAcessorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome')),
                ('data', models.DateField(blank=True, null=True, verbose_name='Data')),
                ('autor', models.CharField(blank=True, max_length=50, verbose_name='Autor')),
                ('ementa', models.TextField(blank=True, verbose_name='Ementa')),
                ('indexacao', models.TextField(blank=True)),
                ('arquivo', models.FileField(blank=True, null=True, upload_to=sapl.utils.texto_upload_path, validators=[sapl.utils.restringe_tipos_de_arquivo_txt], verbose_name='Texto Integral')),
            ],
            options={
                'verbose_name': 'Documento Acessório',
                'verbose_name_plural': 'Documentos Acessórios',
            },
        ),
        migrations.CreateModel(
            name='MateriaAssunto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materia.AssuntoMateria')),
            ],
            options={
                'verbose_name': 'Relação Matéria - Assunto',
                'verbose_name_plural': 'Relações Matéria - Assunto',
            },
        ),
        migrations.CreateModel(
            name='MateriaLegislativa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(verbose_name='Número')),
                ('ano', models.PositiveSmallIntegerField(choices=[(2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960), (1959, 1959), (1958, 1958), (1957, 1957), (1956, 1956), (1955, 1955), (1954, 1954), (1953, 1953), (1952, 1952), (1951, 1951), (1950, 1950), (1949, 1949), (1948, 1948), (1947, 1947), (1946, 1946), (1945, 1945), (1944, 1944), (1943, 1943), (1942, 1942), (1941, 1941), (1940, 1940), (1939, 1939), (1938, 1938), (1937, 1937), (1936, 1936), (1935, 1935), (1934, 1934), (1933, 1933), (1932, 1932), (1931, 1931), (1930, 1930), (1929, 1929), (1928, 1928), (1927, 1927), (1926, 1926), (1925, 1925), (1924, 1924), (1923, 1923), (1922, 1922), (1921, 1921), (1920, 1920), (1919, 1919), (1918, 1918), (1917, 1917), (1916, 1916), (1915, 1915), (1914, 1914), (1913, 1913), (1912, 1912), (1911, 1911), (1910, 1910), (1909, 1909), (1908, 1908), (1907, 1907), (1906, 1906), (1905, 1905), (1904, 1904), (1903, 1903), (1902, 1902), (1901, 1901), (1900, 1900), (1899, 1899), (1898, 1898), (1897, 1897), (1896, 1896), (1895, 1895), (1894, 1894), (1893, 1893), (1892, 1892), (1891, 1891), (1890, 1890)], verbose_name='Ano')),
                ('numero_protocolo', models.PositiveIntegerField(blank=True, null=True, verbose_name='Núm. Protocolo')),
                ('data_apresentacao', models.DateField(verbose_name='Data Apresentação')),
                ('tipo_apresentacao', models.CharField(blank=True, choices=[('O', 'Oral'), ('E', 'Escrita')], max_length=1, verbose_name='Tipo de Apresentação')),
                ('data_publicacao', models.DateField(blank=True, null=True, verbose_name='Data Publicação')),
                ('numero_origem_externa', models.CharField(blank=True, max_length=5, verbose_name='Número')),
                ('ano_origem_externa', models.PositiveSmallIntegerField(blank=True, choices=[(2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960), (1959, 1959), (1958, 1958), (1957, 1957), (1956, 1956), (1955, 1955), (1954, 1954), (1953, 1953), (1952, 1952), (1951, 1951), (1950, 1950), (1949, 1949), (1948, 1948), (1947, 1947), (1946, 1946), (1945, 1945), (1944, 1944), (1943, 1943), (1942, 1942), (1941, 1941), (1940, 1940), (1939, 1939), (1938, 1938), (1937, 1937), (1936, 1936), (1935, 1935), (1934, 1934), (1933, 1933), (1932, 1932), (1931, 1931), (1930, 1930), (1929, 1929), (1928, 1928), (1927, 1927), (1926, 1926), (1925, 1925), (1924, 1924), (1923, 1923), (1922, 1922), (1921, 1921), (1920, 1920), (1919, 1919), (1918, 1918), (1917, 1917), (1916, 1916), (1915, 1915), (1914, 1914), (1913, 1913), (1912, 1912), (1911, 1911), (1910, 1910), (1909, 1909), (1908, 1908), (1907, 1907), (1906, 1906), (1905, 1905), (1904, 1904), (1903, 1903), (1902, 1902), (1901, 1901), (1900, 1900), (1899, 1899), (1898, 1898), (1897, 1897), (1896, 1896), (1895, 1895), (1894, 1894), (1893, 1893), (1892, 1892), (1891, 1891), (1890, 1890)], null=True, verbose_name='Ano')),
                ('data_origem_externa', models.DateField(blank=True, null=True, verbose_name='Data')),
                ('apelido', models.CharField(blank=True, max_length=50, verbose_name='Apelido')),
                ('dias_prazo', models.PositiveIntegerField(blank=True, null=True, verbose_name='Dias Prazo')),
                ('data_fim_prazo', models.DateField(blank=True, null=True, verbose_name='Data Fim Prazo')),
                ('em_tramitacao', models.BooleanField(choices=[(1, 'Sim'), (0, 'Não')], default=False, verbose_name='Em Tramitação?')),
                ('polemica', models.NullBooleanField(verbose_name='Matéria Polêmica?')),
                ('objeto', models.CharField(blank=True, max_length=150, verbose_name='Objeto')),
                ('complementar', models.NullBooleanField(verbose_name='É Complementar?')),
                ('ementa', models.TextField(verbose_name='Ementa')),
                ('indexacao', models.TextField(blank=True, verbose_name='Indexação')),
                ('observacao', models.TextField(blank=True, verbose_name='Observação')),
                ('resultado', models.TextField(blank=True)),
                ('texto_original', models.FileField(blank=True, null=True, upload_to=sapl.utils.texto_upload_path, validators=[sapl.utils.restringe_tipos_de_arquivo_txt], verbose_name='Texto Original')),
                ('anexadas', models.ManyToManyField(blank=True, related_name='anexo_de', through='materia.Anexada', to='materia.MateriaLegislativa')),
                ('autores', models.ManyToManyField(through='materia.Autoria', to='base.Autor')),
            ],
            options={
                'verbose_name': 'Matéria Legislativa',
                'verbose_name_plural': 'Matérias Legislativas',
            },
        ),
        migrations.CreateModel(
            name='Numeracao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_materia', models.CharField(max_length=5, verbose_name='Número')),
                ('ano_materia', models.PositiveSmallIntegerField(choices=[(2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960), (1959, 1959), (1958, 1958), (1957, 1957), (1956, 1956), (1955, 1955), (1954, 1954), (1953, 1953), (1952, 1952), (1951, 1951), (1950, 1950), (1949, 1949), (1948, 1948), (1947, 1947), (1946, 1946), (1945, 1945), (1944, 1944), (1943, 1943), (1942, 1942), (1941, 1941), (1940, 1940), (1939, 1939), (1938, 1938), (1937, 1937), (1936, 1936), (1935, 1935), (1934, 1934), (1933, 1933), (1932, 1932), (1931, 1931), (1930, 1930), (1929, 1929), (1928, 1928), (1927, 1927), (1926, 1926), (1925, 1925), (1924, 1924), (1923, 1923), (1922, 1922), (1921, 1921), (1920, 1920), (1919, 1919), (1918, 1918), (1917, 1917), (1916, 1916), (1915, 1915), (1914, 1914), (1913, 1913), (1912, 1912), (1911, 1911), (1910, 1910), (1909, 1909), (1908, 1908), (1907, 1907), (1906, 1906), (1905, 1905), (1904, 1904), (1903, 1903), (1902, 1902), (1901, 1901), (1900, 1900), (1899, 1899), (1898, 1898), (1897, 1897), (1896, 1896), (1895, 1895), (1894, 1894), (1893, 1893), (1892, 1892), (1891, 1891), (1890, 1890)], verbose_name='Ano')),
                ('data_materia', models.DateField(verbose_name='Data')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materia.MateriaLegislativa')),
            ],
            options={
                'ordering': ('materia', 'tipo_materia', 'numero_materia', 'ano_materia', 'data_materia'),
                'verbose_name': 'Numeração',
                'verbose_name_plural': 'Numerações',
            },
        ),
        migrations.CreateModel(
            name='Orgao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60, verbose_name='Nome')),
                ('sigla', models.CharField(max_length=10, verbose_name='Sigla')),
                ('unidade_deliberativa', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Unidade Deliberativa')),
                ('endereco', models.CharField(blank=True, max_length=100, verbose_name='Endereço')),
                ('telefone', models.CharField(blank=True, max_length=50, verbose_name='Telefone')),
            ],
            options={
                'verbose_name': 'Órgão',
                'verbose_name_plural': 'Órgãos',
            },
        ),
        migrations.CreateModel(
            name='Origem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=10, verbose_name='Sigla')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Origem',
                'verbose_name_plural': 'Origens',
            },
        ),
        migrations.CreateModel(
            name='Parecer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_conclusao', models.CharField(blank=True, max_length=3)),
                ('tipo_apresentacao', models.CharField(choices=[('O', 'Oral'), ('E', 'Escrita')], max_length=1)),
                ('parecer', models.TextField(blank=True)),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materia.MateriaLegislativa')),
            ],
            options={
                'verbose_name': 'Parecer',
                'verbose_name_plural': 'Pareceres',
            },
        ),
        migrations.CreateModel(
            name='Proposicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_envio', models.DateTimeField(blank=True, null=True, verbose_name='Data de Envio')),
                ('data_recebimento', models.DateTimeField(blank=True, null=True, verbose_name='Data de Recebimento')),
                ('data_devolucao', models.DateTimeField(blank=True, null=True, verbose_name='Data de Devolução')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('justificativa_devolucao', models.CharField(blank=True, max_length=200, verbose_name='Justificativa da Devolução')),
                ('ano', models.PositiveSmallIntegerField(blank=True, choices=[(2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960), (1959, 1959), (1958, 1958), (1957, 1957), (1956, 1956), (1955, 1955), (1954, 1954), (1953, 1953), (1952, 1952), (1951, 1951), (1950, 1950), (1949, 1949), (1948, 1948), (1947, 1947), (1946, 1946), (1945, 1945), (1944, 1944), (1943, 1943), (1942, 1942), (1941, 1941), (1940, 1940), (1939, 1939), (1938, 1938), (1937, 1937), (1936, 1936), (1935, 1935), (1934, 1934), (1933, 1933), (1932, 1932), (1931, 1931), (1930, 1930), (1929, 1929), (1928, 1928), (1927, 1927), (1926, 1926), (1925, 1925), (1924, 1924), (1923, 1923), (1922, 1922), (1921, 1921), (1920, 1920), (1919, 1919), (1918, 1918), (1917, 1917), (1916, 1916), (1915, 1915), (1914, 1914), (1913, 1913), (1912, 1912), (1911, 1911), (1910, 1910), (1909, 1909), (1908, 1908), (1907, 1907), (1906, 1906), (1905, 1905), (1904, 1904), (1903, 1903), (1902, 1902), (1901, 1901), (1900, 1900), (1899, 1899), (1898, 1898), (1897, 1897), (1896, 1896), (1895, 1895), (1894, 1894), (1893, 1893), (1892, 1892), (1891, 1891), (1890, 1890)], default=None, null=True, verbose_name='Ano')),
                ('numero_proposicao', models.PositiveIntegerField(blank=True, null=True, verbose_name='Número')),
                ('status', models.CharField(blank=True, choices=[('E', 'Enviada'), ('R', 'Recebida'), ('I', 'Incorporada')], max_length=1, verbose_name='Status Proposição')),
                ('texto_original', models.FileField(blank=True, null=True, upload_to=sapl.utils.texto_upload_path, validators=[sapl.utils.restringe_tipos_de_arquivo_txt], verbose_name='Texto Original')),
                ('object_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('autor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.Autor')),
                ('content_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='Tipo de Material Gerado')),
                ('materia_de_vinculo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='proposicao_set', to='materia.MateriaLegislativa', verbose_name='Matéria anexadora')),
            ],
            options={
                'permissions': (('detail_proposicao_enviada', 'Pode acessar detalhes de uma proposição enviada.'), ('detail_proposicao_devolvida', 'Pode acessar detalhes de uma proposição devolvida.'), ('detail_proposicao_incorporada', 'Pode acessar detalhes de uma proposição incorporada.')),
                'verbose_name': 'Proposição',
                'verbose_name_plural': 'Proposições',
            },
        ),
        migrations.CreateModel(
            name='RegimeTramitacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Regime Tramitação',
                'verbose_name_plural': 'Regimes Tramitação',
            },
        ),
        migrations.CreateModel(
            name='Relatoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_designacao_relator', models.DateField(verbose_name='Data Designação')),
                ('data_destituicao_relator', models.DateField(blank=True, null=True, verbose_name='Data Destituição')),
                ('comissao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='comissoes.Comissao', verbose_name='Comissão')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materia.MateriaLegislativa')),
                ('parlamentar', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='parlamentares.Parlamentar', verbose_name='Parlamentar')),
            ],
            options={
                'verbose_name': 'Relatoria',
                'verbose_name_plural': 'Relatorias',
            },
        ),
        migrations.CreateModel(
            name='StatusTramitacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=10, verbose_name='Sigla')),
                ('descricao', models.CharField(max_length=60, verbose_name='Descrição')),
                ('indicador', models.CharField(blank=True, choices=[('F', 'Fim'), ('R', 'Retorno')], max_length=1, verbose_name='Indicador da Tramitação')),
            ],
            options={
                'ordering': ['descricao'],
                'verbose_name': 'Status de Tramitação',
                'verbose_name_plural': 'Status de Tramitação',
            },
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name='Tipo Documento')),
            ],
            options={
                'verbose_name': 'Tipo de Documento',
                'verbose_name_plural': 'Tipos de Documento',
            },
        ),
        migrations.CreateModel(
            name='TipoFimRelatoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name='Tipo Fim Relatoria')),
            ],
            options={
                'verbose_name': 'Tipo Fim de Relatoria',
                'verbose_name_plural': 'Tipos Fim de Relatoria',
            },
        ),
        migrations.CreateModel(
            name='TipoMateriaLegislativa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=5, verbose_name='Sigla')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição ')),
                ('num_automatica', models.BooleanField(default=False)),
                ('quorum_minimo_votacao', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['descricao'],
                'verbose_name': 'Tipo de Matéria Legislativa',
                'verbose_name_plural': 'Tipos de Matérias Legislativas',
            },
        ),
        migrations.CreateModel(
            name='TipoProposicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
                ('object_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('content_type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType', verbose_name='Definição de Tipo')),
                ('perfis', models.ManyToManyField(blank=True, help_text='\n                    Mesmo que em Configurações da Aplicação nas\n                    Tabelas Auxiliares esteja definido que Proposições possam\n                    utilizar Textos Articulados, ao gerar uma proposição,\n                    a solução de Textos Articulados será disponibilizada se\n                    o Tipo escolhido para a Proposição estiver associado a ao\n                    menos um Perfil Estrutural de Texto Articulado.\n                    ', to='compilacao.PerfilEstruturalTextoArticulado', verbose_name='Perfis Estruturais de Textos Articulados')),
            ],
            options={
                'verbose_name': 'Tipo de Proposição',
                'verbose_name_plural': 'Tipos de Proposições',
            },
        ),
        migrations.CreateModel(
            name='Tramitacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_tramitacao', models.DateField(verbose_name='Data Tramitação')),
                ('data_encaminhamento', models.DateField(blank=True, null=True, verbose_name='Data Encaminhamento')),
                ('urgente', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Urgente ?')),
                ('turno', models.CharField(blank=True, choices=[('P', 'Primeiro'), ('S', 'Segundo'), ('U', 'Único'), ('L', 'Suplementar'), ('F', 'Final'), ('A', 'Votação única em Regime de Urgência'), ('B', '1ª Votação'), ('C', '2ª e 3ª Votação')], max_length=1, verbose_name='Turno')),
                ('texto', models.TextField(verbose_name='Texto da Ação')),
                ('data_fim_prazo', models.DateField(blank=True, null=True, verbose_name='Data Fim Prazo')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materia.MateriaLegislativa')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materia.StatusTramitacao', verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Tramitação',
                'verbose_name_plural': 'Tramitações',
            },
        ),
        migrations.CreateModel(
            name='UnidadeTramitacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comissao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='comissoes.Comissao', verbose_name='Comissão')),
                ('orgao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='materia.Orgao', verbose_name='Órgão')),
                ('parlamentar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='parlamentares.Parlamentar', verbose_name='Parlamentar')),
            ],
            options={
                'verbose_name': 'Unidade de Tramitação',
                'verbose_name_plural': 'Unidades de Tramitação',
            },
        ),
        migrations.AddField(
            model_name='tramitacao',
            name='unidade_tramitacao_destino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tramitacoes_destino', to='materia.UnidadeTramitacao', verbose_name='Unidade Destino'),
        ),
        migrations.AddField(
            model_name='tramitacao',
            name='unidade_tramitacao_local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tramitacoes_origem', to='materia.UnidadeTramitacao', verbose_name='Unidade Local'),
        ),
        migrations.AddField(
            model_name='relatoria',
            name='tipo_fim_relatoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='materia.TipoFimRelatoria', verbose_name='Motivo Fim Relatoria'),
        ),
        migrations.AddField(
            model_name='proposicao',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materia.TipoProposicao', verbose_name='Tipo'),
        ),
        migrations.AddField(
            model_name='parecer',
            name='relatoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materia.Relatoria'),
        ),
        migrations.AddField(
            model_name='numeracao',
            name='tipo_materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materia.TipoMateriaLegislativa', verbose_name='Tipo de Matéria'),
        ),
        migrations.AddField(
            model_name='materialegislativa',
            name='local_origem_externa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='materia.Origem', verbose_name='Local Origem'),
        ),
        migrations.AddField(
            model_name='materialegislativa',
            name='regime_tramitacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materia.RegimeTramitacao', verbose_name='Regime Tramitação'),
        ),
        migrations.AddField(
            model_name='materialegislativa',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materia.TipoMateriaLegislativa', verbose_name='Tipo'),
        ),
        migrations.AddField(
            model_name='materialegislativa',
            name='tipo_origem_externa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tipo_origem_externa_set', to='materia.TipoMateriaLegislativa', verbose_name='Tipo'),
        ),
        migrations.AddField(
            model_name='materiaassunto',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materia.MateriaLegislativa'),
        ),
        migrations.AddField(
            model_name='documentoacessorio',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materia.MateriaLegislativa'),
        ),
        migrations.AddField(
            model_name='documentoacessorio',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materia.TipoDocumento', verbose_name='Tipo'),
        ),
        migrations.AddField(
            model_name='despachoinicial',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materia.MateriaLegislativa'),
        ),
        migrations.AddField(
            model_name='autoria',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materia.MateriaLegislativa', verbose_name='Matéria Legislativa'),
        ),
        migrations.AddField(
            model_name='anexada',
            name='materia_anexada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='materia_anexada_set', to='materia.MateriaLegislativa'),
        ),
        migrations.AddField(
            model_name='anexada',
            name='materia_principal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='materia_principal_set', to='materia.MateriaLegislativa'),
        ),
        migrations.AddField(
            model_name='acompanhamentomateria',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materia.MateriaLegislativa'),
        ),
        migrations.AlterUniqueTogether(
            name='tipoproposicao',
            unique_together=set([('content_type', 'object_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='proposicao',
            unique_together=set([('content_type', 'object_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='materialegislativa',
            unique_together=set([('tipo', 'numero', 'ano')]),
        ),
    ]

from datetime import datetime

from django.http import HttpResponse

from base.models import CasaLegislativa
from base.views import ESTADOS
from comissoes.models import Comissao
from materia.models import (Autor, Autoria, MateriaLegislativa, Numeracao,
                            Tramitacao, UnidadeTramitacao)

from django.http import HttpResponse

from parlamentares.models import Parlamentar
from protocoloadm.models import (DocumentoAdministrativo, Protocolo,
                                 TramitacaoAdministrativo)

from sessao.models import OrdemDia, SessaoPlenaria

from .templates import (pdf_capa_processo_gerar,
                        pdf_documento_administrativo_gerar,
                        pdf_espelho_gerar,
                        pdf_materia_gerar,
                        pdf_protocolo_gerar,
                        pdf_etiqueta_protocolo_gerar)


def get_cabecalho(casa):

    cabecalho = {}
    cabecalho["nom_casa"] = casa.nome
    cabecalho["nom_estado"] = "Estado de " + ESTADOS[casa.uf.upper()]
    return cabecalho


def get_imagem(casa):

    if casa.logotipo:
        return casa.logotipo.path
    else:
        # TODO: recuperar de uma variavel de sistema
        return 'static/img/brasao_transp.gif'


def get_rodape(casa):

    if len(casa.cep) == 8:
        cep = casa.cep[:4] + "-" + casa.cep[5:]
    else:
        cep = ""

    linha1 = casa.endereco

    if cep:
        if casa.endereco:
            linha1 = linha1 + " - "
        linha1 = linha1 + "CEP " + cep

    # substituindo nom_localidade por municipio e sgl_uf por uf
    if casa.municipio:
        linha1 = linha1 + " - " + casa.municipio + " " + casa.uf

    if casa.telefone:
        linha1 = linha1 + " Tel.: " + casa.telefone

    if casa.endereco_web:
        linha2 = casa.endereco_web
    else:
        linha2 = ""

    if casa.email:
        if casa.endereco_web:
            linha2 = linha2 + " - "
        linha2 = linha2 + "E-mail: " + casa.email

    data_emissao = datetime.today().strftime("%d/%m/%Y")

    return [linha1, linha2, data_emissao]


def get_materias(mats):

    materias = []
    for materia in mats:
        dic = {}
        dic['titulo'] = materia.tipo.sigla + " " + materia.tipo.descricao \
            + " " + str(materia.numero) + "/" + str(materia.ano)
        dic['txt_ementa'] = materia.ementa

        autores = Autoria.objects.filter(materia=materia)
        dic['nom_autor'] = " "
        for autoria in autores:
            if autoria.autor.parlamentar:
                dic['nom_autor'] = autoria.autor.parlamentar.nome_completo
            elif autoria.autor.comissao:
                dic['nom_autor'] = autoria.autor.comissao.nome

        des_status = ''
        txt_tramitacao = ''

        dic['localizacao_atual'] = " "

        tramitacoes = Tramitacao.objects.filter(
            unidade_tramitacao_destino__isnull=True).order_by(
            'data_tramitacao')

        for tramitacao in tramitacoes:
            des_status = tramitacao.status.descricao
            txt_tramitacao = tramitacao.texto

        # for tramitacao in context.zsql
        #    .tramitacao_obter_zsql(cod_materia
        #        =materia.cod_materia,ind_ult_tramitacao=1):
        #     if tramitacao.cod_unid_tram_dest:
        #         cod_unid_tram = tramitacao.cod_unid_tram_dest
        #     else:
        #         cod_unid_tram = tramitacao.cod_unid_tram_local
        #     for unidade_tramitacao in
        #         context.zsql
        #              .unidade_tramitacao_obter_zsql(
        #                   cod_unid_tramitacao = cod_unid_tram):
        #         if unidade_tramitacao.cod_orgao:
        #             dic['localizacao_atual']=unidade_tramitacao.nom_orgao
        #         else:
        #             dic['localizacao_atual']=unidade_tramitacao.nom_comissao
        #     des_status=tramitacao.des_status
        #     txt_tramitacao=tramitacao.txt_tramitacao

        dic['des_situacao'] = des_status
        dic['ultima_acao'] = txt_tramitacao

        dic['norma_vinculada'] = " "
        # for norma_vinculada in context.zsql
        #     .materia_buscar_norma_juridica_zsql(cod_materia=materia.cod_materia):
        #     dic['norma_vinculada']=
        #       norma_vinculada.des_norma+" "
        #       +str(norma_vinculada.num_norma)+"/"+str(norma_vinculada.ano_norma)

        materias.append(dic)

    return materias


def relatorio_materia(request):
    '''
        pdf_materia_gerar.py
    '''

    response = HttpResponse(content_type='application/pdf')
    response[
        'Content-Disposition'] = 'attachment; filename="relatorio_materia.pdf"'

    casa = CasaLegislativa.objects.first()

    cabecalho = get_cabecalho(casa)
    rodape = get_rodape(casa)
    imagem = get_imagem(casa)

    # TODO pesquisar baseado em filtros
    mats = MateriaLegislativa.objects.all()[:50]

    materias = get_materias(mats)

    pdf = pdf_materia_gerar.principal(None,
                                      imagem,
                                      None,
                                      materias,
                                      cabecalho,
                                      rodape)

    response.write(pdf)

    return response


def get_capa_processo(prot):
    protocolos = []
    for p in prot:
        dic = {}
        dic['numero'] = str(p.numero)
        dic['ano'] = str(p.ano)
        dic['data'] = str(p.data) + ' - ' + str(p.hora)
        dic['txt_assunto'] = p.assunto_ementa
        dic['txt_interessado'] = p.interessado
        dic['nom_autor'] = " "
        dic['titulo'] = " "

        if p.autor is not None:
            for autor in Autor.objects.filter(id=p.autor.id):
                if autor.tipo == 'Parlamentar':
                    for parlamentar in Parlamentar.objects.filter(
                            id=p.autor.parlamentar.id):
                        dic['nom_autor'] = parlamentar.nome_completo or ' '
                elif autor.tipo == 'Comissao':
                    for comissao in Comissao.objects.filter(
                            id=p.autor.comissao.id):
                        dic['nom_autor'] = comissao.nome or ' '
                else:
                    dic['nom_autor'] = autor.nome or ' '
        else:
            dic['nom_autor'] = p.interessado

        dic['natureza'] = ''
        if p.tipo_processo == 0:
            dic['natureza'] = 'Administrativo'
        if p.tipo_processo == 1:
            dic['natureza'] = 'Legislativo'

        dic['ident_processo'] = str(p.tipo_materia) or str(p.tipo_documento)

        dic['sgl_processo'] = str(p.tipo_materia) or str(p.tipo_documento)

        dic['num_materia'] = ''
        for materia in MateriaLegislativa.objects.filter(
                numero_protocolo=p.numero, ano=p.ano):
            dic['num_materia'] = str(materia.numero) + '/' + str(materia.ano)

        dic['num_documento'] = ''
        for documento in DocumentoAdministrativo.objects.filter(
                numero=p.numero):
            dic['num_documento'] = str(
                documento.numero) + '/' + str(documento.ano)

        dic['num_processo'] = dic['num_materia'] or dic['num_documento']

        dic['numeracao'] = ''
        for materia_num in MateriaLegislativa.objects.filter(
                numero_protocolo=p.numero, ano=p.ano):
            for numera in Numeracao.objects.filter(materia=materia_num):
                dic['numeracao'] = 'PROCESSO N&#176; ' + \
                    str(numera.numero) + '/' + str(numera.ano)

        dic['anulado'] = ''
        if p.anulado == 1:
            dic['anulado'] = 'Nulo'

        protocolos.append(dic)
    return protocolos


def relatorio_processo(request):
    '''
        pdf_capa_processo_gerar.py
    '''

    response = HttpResponse(content_type='application/pdf')
    response[
        'Content-Disposition'] = 'attachment; filename="relatorio_processo.pdf"'

    casa = CasaLegislativa.objects.first()

    cabecalho = get_cabecalho(casa)
    rodape = get_rodape(casa)
    imagem = get_imagem(casa)

    protocolos = Protocolo.objects.all()[:50]
    protocolos_pdf = get_capa_processo(protocolos)

    pdf = pdf_capa_processo_gerar.principal(None,
                                            imagem,
                                            None,
                                            protocolos_pdf,
                                            cabecalho,
                                            rodape)

    response.write(pdf)

    return response


def get_ordem_dia(ordem, sessao):
    pass

    # splen = []
    # pauta = []
    # data = ''

    # for dat_sessao in SessaoPlenaria.objects.filter(id=sessao.id):
    #     data = dat_sessao.data_inicio
    #     dat_ordem = dat_sessao.data_inicio

    # seleciona dados da sessão plenária
    # for sp in context.zsql.sessao_plenaria_obter_zsql(dat_inicio_sessao=data, ind_excluido=0):
    # dicsp = {} # dicionário que armazenará os dados a serem impressos de uma sessão plenária
    #     ts = context.zsql.tipo_sessao_plenaria_obter_zsql(tip_sessao=sp.tip_sessao)[0]
    #     dicsp["sessao"] = str(sp.num_sessao_plen)+"ª Sessao "+ts.nom_sessao+" da "+str(sp.num_sessao_leg)+"ª Sessao Legislativa da "+str(sp.num_legislatura)+"ª Legislatura"
    #     dia = context.pysc.data_converter_por_extenso_pysc(data=sp.dat_inicio_sessao)
    #     hora = context.pysc.hora_formatar_pysc(hora=sp.hr_inicio_sessao)
    #     dicsp["datasessao"] = "Dia "+str(dia)+" ("+str(sp.dia_sessao)+") - Inicio as "+hora
    #     splen.append(dicsp)
    # seleciona as matérias que compõem a pauta na data escolhida
    # for ordem in context.zsql.ordem_dia_obter_zsql(dat_ordem=data, ind_excluido=0):
    # seleciona os detalhes de uma matéria
    #     materia = context.zsql.materia_obter_zsql(cod_materia=ordem.cod_materia)[0]
    # dic = {} # dicionário que armazenará os dados a serem impressos de uma matéria
    #     dic["num_ordem"] = ordem.num_ordem
    #     dic["id_materia"] = materia.des_tipo_materia+" - Nº "+str(materia.num_ident_basica)+"/"+str(materia.ano_ident_basica)
    # dic["id_materia"] = materia.sgl_tipo_materia+" - "+str(materia.num_ident_basica)+"/"+str(materia.ano_ident_basica)+" - "+materia.des_tipo_materia
    #     dic["txt_ementa"] = ordem.txt_observacao
    # numeracao do processo 26/02/2011
    #     dic["des_numeracao"]=""
    #     numeracao = context.zsql.numeracao_obter_zsql(cod_materia=ordem.cod_materia)
    #     if len(numeracao):
    #        numeracao = numeracao[0]
    #        dic["des_numeracao"] = str(numeracao.num_materia)+"/"+str(numeracao.ano_materia)
    #     dic["des_turno"]=""
    #     dic["des_situacao"] = ""
    #     tramitacao = context.zsql.tramitacao_obter_zsql(cod_materia=ordem.cod_materia, ind_ult_tramitacao=1)
    #     if len(tramitacao):
    #         tramitacao = tramitacao[0]
    #         if tramitacao.sgl_turno != "":
    #             for turno in [("P","Primeiro"), ("S","Segundo"), ("U","Único"), ("L","Suplementar"), ("A","Votação Única em Regime de Urgência"), ("B","1ª Votação"), ("C","2ª e 3ª Votações")]:
    #                 if tramitacao.sgl_turno == turno[0]:
    #                     dic["des_turno"] = turno[1]

    #         dic["des_situacao"] = tramitacao.des_status
    #         if dic["des_situacao"]==None:
    #              dic["des_situacao"] = " "

    #     dic["nom_autor"] = ''
    #     autoria = context.zsql.autoria_obter_zsql(cod_materia=ordem.cod_materia, ind_primeiro_autor=1)
    # if len(autoria): # se existe autor
    #         autoria = autoria[0]
    #     try:
    #       autor = context.zsql.autor_obter_zsql(cod_autor=autoria.cod_autor)
    #       if len(autor):
    #          autor = autor[0]

    #       if autor.des_tipo_autor == "Parlamentar":
    #          parlamentar = context.zsql.parlamentar_obter_zsql(cod_parlamentar=autor.cod_parlamentar)[0]
    #          dic["nom_autor"] = parlamentar.nom_parlamentar

    #       elif autor.des_tipo_autor == "Comissao":
    #            comissao = context.zsql.comissao_obter_zsql(cod_comissao=autor.cod_comissao)[0]
    #            dic["nom_autor"] = comissao.nom_comissao
    #       else:
    #            dic["nom_autor"] = autor.nom_autor
    #     except:
    #       pass
    # lst_relator = [] # lista contendo os relatores da matéria
    #     for relatoria in context.zsql.relatoria_obter_zsql(cod_materia=ordem.cod_materia):
    #         parlamentar = context.zsql.parlamentar_obter_zsql(cod_parlamentar=relatoria.cod_parlamentar)[0]
    #         comissao = context.zsql.comissao_obter_zsql(cod_comissao=relatoria.cod_comissao)[0]
    #         lst_relator.append(parlamentar.nom_parlamentar+" - "+comissao.nom_comissao)
    #     if not len(lst_relator):
    #         lst_relator = ['']
    #     dic["lst_relator"] = lst_relator

    # adiciona o dicionário na pauta
    #     pauta.append(dic)


def relatorio_ordem_dia(request):
    '''
        pdf_ordem_dia_gerar.py
    '''

    response = HttpResponse(content_type='application/pdf')

    response[
        'Content-Disposition'] = 'attachment; filename="relatorio_ordem_dia.pdf"'

    casa = CasaLegislativa.objects.first()

    cabecalho = get_cabecalho(casa)
    rodape = get_rodape(casa)
    imagem = get_imagem(casa)

    ordem = OrdemDia.objects.all()[:50]
    sessao = SessaoPlenaria.objects.first()
    ordem_pdf = get_ordem_dia(ordem, sessao)

    pdf = pdf_capa_processo_gerar.principal(None,
                                            imagem,
                                            None,
                                            ordem_pdf,
                                            cabecalho,
                                            rodape)

    response.write(pdf)

    return response


def relatorio_documento_administrativo(request):
    '''
        pdf_documento_administrativo_gerar.py
    '''

    response = HttpResponse(content_type='application/pdf')
    response[
        'Content-Disposition'] = 'attachment; filename="relatorio_documento_administrativo.pdf"'

    casa = CasaLegislativa.objects.first()

    cabecalho = get_cabecalho(casa)
    rodape = get_rodape(casa)
    imagem = get_imagem(casa)

    docs = DocumentoAdministrativo.objects.all()[:50]
    doc_pdf = get_documento_administrativo(docs)

    pdf = pdf_documento_administrativo_gerar.principal(
        None,
        imagem,
        None,
        doc_pdf,
        cabecalho,
        rodape)
    response.write(pdf)

    return response


def get_documento_administrativo(docs):

    documentos = []
    for d in docs:
        dic = {}
        dic['titulo'] = str(d)
        dic['txt_assunto'] = d.assunto
        dic['txt_interessado'] = d.interessado

        des_status = ''
        txt_tramitacao = ''

        dic['localizacao_atual'] = ' '
        # Será removido o 'última'?
        for t in TramitacaoAdministrativo.objects.filter(
                documento=d, ultima=True):
            if t.unidade_tramitacao_destino:
                cod_unid_tram = t.unidade_tramitacao_destino
            else:
                cod_unid_tram = t.unidade_tramitacao_destino

            for unidade_tramitacao in UnidadeTramitacao.objects.filter(
                    id=cod_unid_tram):
                if unidade_tramitacao.orgao:
                    dic['localizacao_atual'] = unidade_tramitacao.orgao
                else:
                    dic['localizacao_atual'] = unidade_tramitacao.comissao

            des_status = t.status.descricao
            txt_tramitacao = t.texto

        dic['des_situacao'] = des_status
        dic['ultima_acao'] = txt_tramitacao

        documentos.append(dic)
    return documentos


def relatorio_espelho(request):
    '''
        pdf_espelho_gerar.py
    '''

    response = HttpResponse(content_type='application/pdf')
    response[
        'Content-Disposition'] = 'attachment; filename="relatorio_espelho.pdf"'

    casa = CasaLegislativa.objects.first()

    cabecalho = get_cabecalho(casa)
    rodape = get_rodape(casa)
    imagem = get_imagem(casa)

    mats = MateriaLegislativa.objects.all()[:50]
    mat_pdf = get_espelho(mats)

    pdf = pdf_espelho_gerar.principal(
        None,
        imagem,
        None,
        mat_pdf,
        cabecalho,
        rodape)
    response.write(pdf)

    return response


def get_espelho(mats):
    materias = []
    for m in mats:
        dic = {}
        dic['titulo'] = str(m)
        dic['materia'] = str(m.numero) + '/' + str(m.ano)
        dic['dat_apresentacao'] = str(m.data_apresentacao)
        dic['txt_ementa'] = m.ementa

        dic['nom_autor'] = ' '
        for autoria in Autoria.objects.filter(materia=m, primeiro_autor=True):
            for autor in Autor.objects.filter(id=autoria.autor.id):
                if autor.tipo == 'Parlamentar':
                    for parlamentar in Parlamentar.objects.filter(
                            id=autor.parlamentar.id):
                        dic['nom_autor'] = parlamentar.nome_completo
                elif autor.tipo == 'Comissao':
                    for comissao in Comissao.objects.filter(
                            id=autor.comissao.id):
                        dic['nom_autor'] = str(comissao)
                else:
                    dic['nom_autor'] = autor.nome

        des_status = ''
        txt_tramitacao = ''
        data_ultima_acao = ''

        dic['localizacao_atual'] = " "
        for tramitacao in Tramitacao.objects.filter(materia=m):
            if tramitacao.unidade_tramitacao_destino:
                cod_unid_tram = tramitacao.unidade_tramitacao_destino
            else:
                cod_unid_tram = tramitacao.unidade_tramitacao_local

            for unidade_tramitacao in UnidadeTramitacao.objects.filter(
                    id=cod_unid_tram.id):
                if unidade_tramitacao.orgao:
                    dic['localizacao_atual'] = unidade_tramitacao.orgao
                elif unidade_tramitacao.parlamentar:
                    dic['localizacao_atual'] = unidade_tramitacao.parlamentar
                else:
                    dic['localizacao_atual'] = unidade_tramitacao.comissao

            des_status = tramitacao.status
            txt_tramitacao = tramitacao.texto
            data_ultima_acao = tramitacao.data_tramitacao

        dic['des_situacao'] = des_status
        dic['ultima_acao'] = txt_tramitacao
        dic['data_ultima_acao'] = data_ultima_acao

        dic['norma_juridica_vinculada'] = 'Não há nenhuma\
                                           norma jurídica vinculada'
        # TODO
        # for norma in context.zsql.materia_buscar_norma_juridica_zsql(cod_materia=materia.cod_materia):
        #     dic['norma_juridica_vinculada'] = norma.des_norma + " " + \
        #         str(norma.num_norma) + "/" + str(norma.ano_norma)

        materias.append(dic)
    return materias


def get_protocolos(prots):

    protocolos = []
    for protocolo in prots:
        dic = {}

        dic['titulo'] = str(protocolo.numero) + '/' + str(protocolo.ano)

        dic['data'] = protocolo.data.strftime(
            "%d/%m/%Y") + ' - <b>Horário:</b>' + protocolo.hora.strftime("%H:%m")

        dic['txt_assunto'] = protocolo.assunto_ementa

        dic['txt_interessado'] = protocolo.interessado

        dic['nom_autor'] = " "

        if protocolo.autor:
            if protocolo.autor.parlamentar:
                dic['nom_autor'] = protocolo.autor.parlamentar.nome_completo
            elif protocolo.autor.comissao:
                dic['nom_autor'] = protocolo.autor.comissao.nome

        dic['natureza'] = ''

        if protocolo.tipo_documento:
            dic['natureza'] = 'Administrativo'
            dic['processo'] = protocolo.tipo_documento.descricao
        elif protocolo.tipo_materia:
            dic['natureza'] = 'Legislativo'
            dic['processo'] = protocolo.tipo_materia.descricao
        else:
            dic['natureza'] = 'Indefinida'
            dic['processo'] = ''

        dic['anulado'] = ''
        if protocolo.anulado:
            dic['anulado'] = 'Nulo'

        protocolos.append(dic)

    return protocolos


def relatorio_protocolo(request):
    '''
        pdf_protocolo_gerar.py
    '''

    response = HttpResponse(content_type='application/pdf')
    response[
        'Content-Disposition'] = 'attachment; filename="relatorio_protocolo.pdf"'

    casa = CasaLegislativa.objects.first()

    cabecalho = get_cabecalho(casa)
    rodape = get_rodape(casa)
    imagem = get_imagem(casa)

    protocolos = Protocolo.objects.all()[:50]

    protocolo_data = get_protocolos(protocolos)

    pdf = pdf_protocolo_gerar.principal(None,
                                        imagem,
                                        None,
                                        protocolo_data,
                                        cabecalho,
                                        rodape)

    response.write(pdf)

    return response


def relatorio_etiqueta_protocolo(request):
    '''
        pdf__etiqueta_protocolo_gerar.py
    '''

    response = HttpResponse(content_type='application/pdf')
    response[
        'Content-Disposition'] = 'attachment; filename="relatorio_etiqueta_protocolo.pdf"'

    casa = CasaLegislativa.objects.first()

    cabecalho = get_cabecalho(casa)
    rodape = get_rodape(casa)
    imagem = get_imagem(casa)

    protocolos = Protocolo.objects.all()[:50]

    protocolo_data = get_etiqueta_protocolos(protocolos)

    pdf = pdf_etiqueta_protocolo_gerar.principal(None,
                                                 imagem,
                                                 None,
                                                 protocolo_data,
                                                 cabecalho,
                                                 rodape)

    response.write(pdf)

    return response


def get_etiqueta_protocolos(prots):

    protocolos = []
    for p in prots:
        dic = {}

        dic['titulo'] = str(p.numero) + '/' + str(p.ano)
        dic['data'] = p.data.strftime(
            "%d/%m/%Y") + ' - <b>Horário:</b>' + p.hora.strftime("%H:%m")
        dic['txt_assunto'] = p.assunto_ementa
        dic['txt_interessado'] = p.interessado

        dic['nom_autor'] = ' '

        if p.autor:
            if p.autor.parlamentar:
                dic['nom_autor'] = p.autor.parlamentar.nome_completo
            elif p.autor.comissao:
                dic['nom_autor'] = p.autor.comissao.nome

        dic['natureza'] = ''
        if p.tipo_processo == 0:
            dic['natureza'] = 'Administrativo'
        if p.tipo_processo == 1:
            dic['natureza'] = 'Legislativo'

        dic['num_materia'] = ''
        for materia in MateriaLegislativa.objects.filter(
                numero_protocolo=p.numero, ano=p.ano):
            dic['num_materia'] = str(materia)

        dic['num_documento'] = ''
        for documento in DocumentoAdministrativo.objects.filter(
                numero_protocolo=p.numero):
            dic['num_documento'] = str(documento)

        dic['ident_processo'] = dic['num_materia'] or dic['num_documento']

        dic['processo'] = (str(p.tipo_materia) or
                           str(p.tipo_documento))

        dic['anulado'] = ''
        if p.anulado:
            dic['anulado'] = 'Nulo'

        protocolos.append(dic)
    return protocolos
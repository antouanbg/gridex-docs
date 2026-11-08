import json
import os
from integrations import chapters as integration_chapters
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Flowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image as PILImage

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
OUT=ROOT/'static/downloads'
OUT.mkdir(parents=True,exist_ok=True)
FONT=Path(os.environ.get('GRIDEX_PDF_FONT_DIR','/usr/share/fonts/truetype/dejavu'))
for name,file in [('GX','DejaVuSans.ttf'),('GXB','DejaVuSans-Bold.ttf')]:
 pdfmetrics.registerFont(TTFont(name,str(FONT/file)))
pdfmetrics.registerFontFamily('GX',normal='GX',bold='GXB',italic='GX',boldItalic='GXB')
GREEN=colors.HexColor('#0A4435'); INK=colors.HexColor('#203E35'); PALE=colors.HexColor('#EFF6F1'); LIME=colors.HexColor('#C1E84D'); MUTED=colors.HexColor('#62776E')
styles={k:ParagraphStyle(k,fontName=f,fontSize=s,leading=l,textColor=c,spaceAfter=a) for k,f,s,l,c,a in [
 ('body','GX',10.4,16,INK,12),('small','GX',8.2,12,MUTED,9),('h1','GXB',24,30,GREEN,17),('h2','GXB',13,18,GREEN,9),('cell','GX',9.2,14,INK,0),('head','GXB',9.2,14,colors.white,0),('cover','GXB',39,47,GREEN,20),('toc','GX',9.5,15,INK,0)]}
def clean(s):
 return s.replace('Издание 3.0','Издание 5.0').replace('Edition 3.0','Edition 5.0').replace('—','-').replace('–','-').replace('\u2011','-')
def p(t,k='body'):return Paragraph(clean(t),styles[k])
def table(rows):
 t=Table(rows,colWidths=[155,344],repeatRows=1,hAlign='LEFT')
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),GREEN),('ROWBACKGROUNDS',(0,1),(-1,-1),[PALE,colors.white]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),11),('RIGHTPADDING',(0,0),(-1,-1),11),('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),10),('LINEBELOW',(0,1),(-1,-1),.4,colors.HexColor('#D8E5DC'))]))
 return t
class Doc(SimpleDocTemplate):
 def afterFlowable(self,flow):
  if isinstance(flow,Paragraph) and getattr(flow,'bookmark',None):
   key=flow.bookmark; self.canv.bookmarkPage(key); self.canv.addOutlineEntry(flow.getPlainText(),key,level=0)
class ScreenPart(Flowable):
 def __init__(self,path,start,end,width=470):
  Flowable.__init__(self)
  self.path=str(path); self.start=start; self.end=end
  self.pw,self.ph=PILImage.open(path).size
  self.width=width; self.scale=width/self.pw; self.height=(end-start)*self.scale
 def draw(self):
  c=self.canv;c.saveState();clip=c.beginPath();clip.rect(0,0,self.width,self.height);c.clipPath(clip,stroke=0)
  c.drawImage(ImageReader(self.path),0,self.height-(self.ph-self.start)*self.scale,width=self.width,height=self.ph*self.scale)
  c.restoreState()
def frame(c,d):
 c.saveState();c.setFillColor(GREEN);c.rect(0,833,595.28,9,fill=1,stroke=0)
 c.setFont('GXB',11);c.drawString(48,808,'GrideX');c.setFont('GX',8);c.setFillColor(MUTED)
 c.drawRightString(547,808,'ПРОДУКТОВА СПЕЦИФИКАЦИЯ | 5.0' if d.bg else 'PRODUCT SPECIFICATION | 5.0')
 c.setStrokeColor(colors.HexColor('#D8E5DC'));c.line(48,43,547,43);c.setFont('GX',8);c.drawString(48,28,'gridex.tech | 08.11.2026');c.drawRightString(547,28,str(d.page));c.restoreState()
base=json.loads((HERE/'v3_base.json').read_text())
technical=json.loads((HERE/'v3_technical.json').read_text())
technical[0][2][0][2]='Каталогът включва интелигентен хибрид, ценови арбитраж, самоконсумация, нулев износ, ограничаване на пиковете, следване на график, резервно захранване и ръчно управление. Раздел „Режим“ показва стратегията на избрания Обект. Активирането следва отделен процес за проверка, одобрение и прилагане.'
technical[0][2][0][3]='The catalogue includes intelligent hybrid, price arbitrage, self-consumption, zero export, peak shaving, schedule following, backup reserve and manual control. Mode shows the selected Site strategy. Activation follows a separate validation, approval and application process.'
technical[3][2][1][2]='Ръчната заявка за мощност изисква отделно право, причина за действието и ограничен срок на валидност. BMS лимитите и блокировките остават с приоритет. Екранът разграничава заявена, потвърдена приложена и действително измерена мощност.'
technical[3][2][1][3]='A manual power request requires a separate permission, action reason and limited validity period. BMS limits and interlocks retain priority. The screen distinguishes requested, confirmed applied and actual measured power.'
technical[8][2][1][2]='Измерване, публикуване и heartbeat имат отделни периоди. Историята съхранява приетите времево означени събития за избраните метрики. Прилагането на профила се проследява чрез потвърждение от устройството. Липсващите стойности и старите измервания запазват действителния си статус и време. Празният период се обозначава като липса на данни.'
technical[8][2][1][3]='Measurement, publication and heartbeat use separate periods. History stores accepted timestamped events for selected metrics. Profile application is tracked through device acknowledgement. Missing values and old measurements retain their actual status and time. An empty period is labelled as no data.'
technical[9][2][1][2]='Референтната ROCK/ESP конфигурация включва един ROCK Pi E и ESP възли с по един CAN или изолиран RS485 порт за свързаното устройство. Драйверът се определя по тип, модел и протокол. Съвместимостта за всеки модел включва регистри, мащабиране, знакова конвенция и допустими команди. Разширяването на списъка следва проверка на точната хардуерна и firmware версия.'
technical[9][2][1][3]='The reference ROCK/ESP configuration includes one ROCK Pi E and ESP nodes with one CAN or isolated RS485 device port each. Drivers are defined by type, model and protocol. Model compatibility covers registers, scaling, sign convention and permitted commands. Catalogue extension follows validation of the exact hardware and firmware version.'
technical[10][2][2][2]='Покани, решения за услуги, предупреждения при прекъсване и клиентски запитвания са отделни процеси. За изпращането се следят резултатът от доставчика и неопределените състояния, за да се ограничат повторенията. Формата за запитване е защитена от автоматизирани злоупотреби. Подраздел „Аларма“ се намира в „Режим“.'
technical[10][2][2][3]='Invitations, service decisions, connectivity alerts and customer enquiries are separate processes. Provider outcomes and uncertain states are tracked to limit repeated messages. The enquiry form is protected against automated abuse. Alarm is located under Mode.'
extensions=json.loads((HERE/'v3_extensions.json').read_text())
chapters=base+[{'title':x[:2],'blocks':x[2]} for x in technical]+extensions+integration_chapters
def build(lang):
 i=0 if lang=='BG' else 1; pick=lambda b,e:b if i==0 else e
 story=[Spacer(1,50),p('GrideX','cover'),p(pick('Енергия. Данни. Управление.','Energy. Data. Control.'),'h1'),p(pick('Пълна продуктова и функционална спецификация','Complete product and functional specification'),'h2'),Spacer(1,20)]
 story.append(table([[p(pick('ЕДНА ПЛАТФОРМА','ONE PLATFORM'),'head'),p(pick('ЕДИНЕН ЕНЕРГИЕН МОДЕЛ','UNIFIED ENERGY MODEL'),'head')]]+[[p(a,'cell'),p(b,'cell')] for a,b in pick([
 ('Обекти и активи','Батерии, инвертори, зарядни станции и товари'),('Инфраструктура','Edge контролери, измерване и защитена комуникация'),('Данни и услуги','Цени, графики, анализ и прогнозни модели'),('Режими и икономика','Стратегии, ограничения, разходи и енергиен баланс')],[('Sites and assets','Batteries, inverters, charging stations and loads'),('Infrastructure','Edge controllers, metering and secure communication'),('Data and services','Prices, charts, analytics and forecast models'),('Modes and economics','Strategies, constraints, costs and energy balance')])]))
 story.extend([Spacer(1,30),p(pick('Издание 3.0 | Български','Edition 3.0 | English'),'h2'),p(pick('Пълен функционален обхват, включително проектни опции. Конкретните активирани модули, интеграции и параметри се определят с клиентската конфигурация и договора.','Full functional scope, including project options. Activated modules, integrations and parameters are defined by the customer configuration and contract.')),p(pick('За собственици на енергийни обекти, организационни администратори, оператори и интегратори.','For energy-site owners, organisation administrators, operators and integrators.'),'small'),PageBreak()])
 story.append(p(pick('Съдържание','Contents'),'h1'))
 story.append(p(pick('Изберете заглавие за преминаване към съответния раздел.','Select a title to navigate to its section.'),'small'))
 for n,ch in enumerate(chapters,1):story.append(p(f'<link href="#ch{n}" color="#0A4435">{n:02d}  {escape(ch["title"][i])}</link>','toc'))
 story.append(p(f'<link href="#screens" color="#0A4435">{len(chapters)+1}  {pick("Примерни екрани по роли","Example screens by role")}</link>','toc'))
 story.append(p(f'<link href="#support" color="#0A4435">{len(chapters)+2}  {pick("Термини, документация и контакт","Terminology, documentation and contact")}</link>','toc'))
 for n,ch in enumerate(chapters,1):
  story.append(PageBreak());story.append(p(f'{n:02d} / '+pick('ПЪЛЕН ПРОДУКТОВ ОБХВАТ','FULL PRODUCT SCOPE'),'small'))
  heading=p(ch['title'][i],'h1');heading.bookmark=f'ch{n}';story.append(heading)
  if 'blocks' in ch:
   for entry in ch['blocks']:
    story.extend([p(entry[i],'h2'),p(entry[2+i])])
  else:
   story.extend([p(ch['location'][i],'small'),p(ch['intro'][i])])
   tab=table([[p(pick('Елемент / настройка','Element / setting'),'head'),p(pick('Описание и приложение','Description and use'),'head')]]+[[p(row[i],'cell'),p(row[2+i],'cell')] for row in ch['rows']])
   if n>27:tab.setStyle(TableStyle([('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
   story.append(tab)
   story.extend([Spacer(1,16),p(pick('Практическо приложение','Practical use'),'h2'),p(ch['detail'][i])])
 screens=ROOT/'static/img/approved'
 examples=[('superadmin','Супер администратор','Super administrator',[(0,1054),(1054,2108)]),('organisation-admin','Администратор на организация','Organisation administrator',[(0,1143),(1143,2286)]),('member','Личен достъп на потребител','Member personal access',[(0,1189)])]
 for role,bg,en,parts in examples:
  for part,(start,end) in enumerate(parts,1):
   story.append(PageBreak()); heading=p(pick(bg,en),'h1')
   if role=='superadmin' and part==1:heading.bookmark='screens'
   story.append(heading)
   story.append(p(pick('Примерен одобрен макет от документацията. Използвани са само примерни самоличности и Обекти.','Approved reference mockup from the documentation, shown in Bulgarian. All identities and Sites are examples.'),'small'))
   story.append(p(pick(f'Част {part} от {len(parts)} · Настройки → Потребители',f'Part {part} of {len(parts)} · Settings → Users'),'small'))
   story.append(ScreenPart(screens/f'users-{role}-1024.png',start,end))
 story.append(PageBreak());heading=p(pick('Термини, документация и контакт','Terminology, documentation and contact'),'h1');heading.bookmark='support';story.append(heading)
 glossary=[('SOC','State of charge','Състояние на заряд'),('SOH','State of health','Оценка за състоянието на батерията'),('PCC','Point of common coupling','Точка на присъединяване'),('BMS / PCS','Battery management / power conversion system','Управление на батерията / силово преобразуване'),('kW / kWh','Power / energy','Мощност / енергия'),('EFC','Equivalent full cycles','Еквивалентни пълни цикли'),('ERP / MES / WMS','Business / manufacturing / warehouse systems','Бизнес / производствена / складова система')]
 story.append(table([[p(pick('Термин','Term'),'head'),p(pick('Значение','Meaning'),'head')]]+[[p(a,'cell'),p(c if i==0 else b,'cell')] for a,b,c in glossary]))
 story.extend([Spacer(1,20),p(pick('Помощ и поддръжка','Help and support'),'h2'),p('gridex.tech<br/>doc.gridex.tech<br/>support@gridex.tech'),p(pick('Основата на спецификацията е продуктовият модел на GrideX: навигация и права, договор за стратегии и настройки, пазарни услуги, Edge интеграция и прогнозен модул. Примерите обясняват методиката; търговските условия и гаранциите са по договор.','The specification is based on the GrideX product model: navigation and permissions, strategy/settings contract, market services, Edge integration and forecast module. Examples explain the method; commercial terms and warranties are contractual.')),p(pick('Suntech STE-261L-125P: характеристиките 125 kW / 261 kWh са по продуктовата информация на производителя. GrideX е проект с отворен код (MIT). Търговските марки принадлежат на съответните им притежатели.','Suntech STE-261L-125P: the 125 kW / 261 kWh ratings follow manufacturer product information. GrideX is an open-source project (MIT). Trademarks belong to their respective owners.'),'small')])
 out=OUT/f'GrideX_Full_Product_Specification_{lang}_2026-11_v5.pdf'
 doc=Doc(str(out),pagesize=(595.28,841.89),leftMargin=48,rightMargin=48,topMargin=65,bottomMargin=58,title=pick('GrideX - Пълна продуктова спецификация','GrideX - Full product specification'),author='GrideX',pageCompression=1);doc.bg=i==0
 doc.build(story,onFirstPage=frame,onLaterPages=frame);print(out)
for lang in ['BG','EN']:build(lang)

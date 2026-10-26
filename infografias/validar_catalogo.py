#!/usr/bin/env python3
"""Valida catálogo y archivos locales. Sin dependencias externas."""
import json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
errors=[]
def check(ok,msg):
 if not ok:errors.append(msg)
def asset(value,label,extensions):
 if not isinstance(value,str) or not re.fullmatch(r'infografias/[A-Za-z0-9_./-]+',value) or '..' in value.split('/'):
  errors.append(label+': ruta local inválida');return
 p=ROOT/value;check(p.is_file(),label+': archivo inexistente '+value);check(p.suffix.lower() in extensions,label+': formato no admitido')
def main():
 try:c=json.loads((ROOT/'infografias/catalogo.json').read_text())
 except (OSError,ValueError) as e:print('ERROR:',e);return 1
 check(c.get('version')==1,'Versión del catálogo inválida')
 cats=c.get('colecciones',[]);items=c.get('infografias',[])
 if not isinstance(cats,list) or not isinstance(items,list):print('ERROR: colecciones/infografias deben ser arreglos');return 1
 ids=set();seen=set()
 for x in cats:
  i=x.get('id');check(bool(i) and i not in ids,'Colección sin identificador único');ids.add(i);check(bool(x.get('titulo')),'Colección sin título')
 for x in items:
  i=x.get('id','(sin id)');check(i not in seen and i!='(sin id)',f'{i}: identificador inválido o duplicado');seen.add(i)
  check(x.get('coleccion') in ids,f'{i}: colección desconocida')
  for field in ['titulo','descripcion','alt','tipo']:check(isinstance(x.get(field),str) and bool(x[field].strip()),f'{i}: falta {field}')
  check(isinstance(x.get('publicado'),bool),f'{i}: publicado debe ser booleano')
  check(isinstance(x.get('etiquetas',[]),list) and all(isinstance(t,str) for t in x.get('etiquetas',[])),f'{i}: etiquetas inválidas')
  credit=x.get('creditos',{});check(isinstance(credit,dict),f'{i}: créditos inválidos')
  if isinstance(credit,dict):
   for f in ['autor','licencia']:check(bool(credit.get(f)),f'{i}: falta crédito {f}')
   check(not credit.get('url') or str(credit['url']).startswith('https://'),f'{i}: fuente debe usar HTTPS')
  formats={'.webp','.jpg','.jpeg','.png','.avif'};asset(x.get('imagen'),f'{i} imagen',formats)
  if x.get('miniatura'):asset(x['miniatura'],f'{i} miniatura',formats)
  if x.get('descarga'):
   if isinstance(x['descarga'],dict):asset(x['descarga'].get('ruta'),f'{i} descarga',formats|{'.pdf'})
   else:errors.append(f'{i}: descarga debe ser objeto o null')
 if errors:print('\n'.join('ERROR: '+s for s in errors));return 1
 print(f'Catálogo válido: {len(cats)} colecciones, {len(items)} materiales, {sum(x.get("publicado") is True for x in items)} publicados.');return 0
if __name__=='__main__':sys.exit(main())

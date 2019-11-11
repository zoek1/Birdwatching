import re

from pypika import Order, functions, Table, Query


def get_wheres(args, attrs):
    where_regex = re.compile(r'^({})(__(gte?|lte?|ne))?$'.format('|'.join(attrs)))
    where = []

    for key, value in args.items():
        if where_regex.match(key):
            type = key.split('__')
            if len(type) > 1:
                where.append({
                    'key': type[0], 'value': value[0], 'type': type[1]
                })
            else:
                where.append({
                    'key': key, 'value': value[0], 'type': 'eq'
                })
    return where

def build_cond(serie, cond):
    print(cond)
    if cond['type'] == 'gt':
        return getattr(serie, cond['key']) > cond['value']
    if cond['type'] == 'gte':
        return getattr(serie, cond['key']) >= cond['value']
    if cond['type'] == 'lt':
        return getattr(serie, cond['key']) < cond['value']
    if cond['type'] == 'lte':
        return getattr(serie, cond['key']) <= cond['value']
    if cond['type'] == 'ne':
        return getattr(serie, cond['key']) != cond['value']

    return getattr(serie, cond['key']) == cond['value']

def build_select(serie, select):
    operation = select.split('__')
    if len(operation) > 1:

        if operation[1] == 'count':
            return functions.Count(getattr(serie, operation[0]))
        if operation[1] == 'sum':
            return functions.Sum(getattr(serie, operation[0]))
        if operation[1] == 'avg':
            return functions.Avg(getattr(serie, operation[0]))
        if operation[1] == 'min':
            return functions.Min(getattr(serie, operation[0]))
        if operation[1] == 'max':
            return functions.Max(getattr(serie, operation[0]))
        if operation[1] == 'std':
            return functions.Std(getattr(serie, operation[0]))
        if operation[1] == 'stddev':
            return functions.StdDev(getattr(serie, operation[0]))
        if operation[1] == 'abs':
            return functions.Abs(getattr(serie, operation[0]))
        if operation[1] == 'first':
            return functions.First(getattr(serie, operation[0]))
        if operation[1] == 'last':
            return functions.Last(getattr(serie, operation[0]))

        return operation[0]

    return select


def build_query(serie, select='*', limit=0, since=False, until=False, order='asc', group='', where=[]):
    serie = Table(serie)
    query = Query.from_(serie)

    if select:
        args = [build_select(serie, s) for s in select.split(',')]
        print(args)
        query = query.select(*args)

    if where:
        for cond in where:
            conditional = build_cond(serie, cond)
            query = query.where(conditional)
    if limit:
        query = query.limit(limit)
    if since:
        query = query.where(serie.time >= since)
    if until:
        query = query.where(serie.time <= until)
    if order == 'desc':
        query = query.orderby(serie.time, order=Order.desc)
    else:
        query = query.orderby(serie.time, order=Order.asc)
    if group:
        query = query.groupby(getattr(serie, group))

    print(query.get_sql())
    return query

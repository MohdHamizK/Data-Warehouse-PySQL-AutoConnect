<mxfile host="app.diagrams.net" agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36" version="27.1.6">
  <diagram id="abc123xyz" name="Page-1">
    <mxGraphModel dx="1042" dy="574" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="dim_date" value="dim_date&lt;br&gt;date_key (PK)&lt;br&gt;full_date&lt;br&gt;day_of_week" style="rounded=1;whiteSpace=wrap;html=1;" parent="1" vertex="1">
          <mxGeometry x="230" y="100" width="160" height="100" as="geometry" />
        </mxCell>
        <mxCell id="dim_customer" value="dim_customer&lt;br&gt;customer_id (PK)&lt;br&gt;first_name&lt;br&gt;last_name" style="rounded=1;whiteSpace=wrap;html=1;" parent="1" vertex="1">
          <mxGeometry x="10" y="200" width="160" height="100" as="geometry" />
        </mxCell>
        <mxCell id="dim_product" value="dim_product&lt;br&gt;product_id (PK)&lt;br&gt;product_name&lt;br&gt;category" style="rounded=1;whiteSpace=wrap;html=1;" parent="1" vertex="1">
          <mxGeometry x="460" y="100" width="160" height="100" as="geometry" />
        </mxCell>
        <mxCell id="dim_store" value="dim_store&lt;br&gt;store_id (PK)&lt;br&gt;store_name&lt;br&gt;location_city" style="rounded=1;whiteSpace=wrap;html=1;" parent="1" vertex="1">
          <mxGeometry x="660" y="230" width="160" height="100" as="geometry" />
        </mxCell>
        <mxCell id="fact_sales" value="fact_sales&lt;br&gt;sale_id (PK)&lt;br&gt;order_id&lt;br&gt;customer_id (FK)&lt;br&gt;product_id (FK)&lt;br&gt;store_id (FK)&lt;br&gt;date_key (FK)" style="shape=table_row;html=1;" parent="1" vertex="1">
          <mxGeometry x="310" y="340" width="200" height="180" as="geometry" />
        </mxCell>
        <mxCell id="e1" parent="1" source="dim_date" target="fact_sales" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e2" parent="1" source="dim_customer" target="fact_sales" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e3" parent="1" source="dim_product" target="fact_sales" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e4" parent="1" source="dim_store" target="fact_sales" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>

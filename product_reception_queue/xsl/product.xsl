<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/productcollection">
<products>

    <xsl:for-each select="product">

        <xsl:sort select="@id"/>

        <product>
            <category>
            
                <xsl:value-of select="category"/>        

            </category>
            <name>
            
                <xsl:value-of select="name"/>        

            </name>
            <description>
            
                <xsl:value-of select="description"/>        

            </description>
            <price>
            
                <xsl:value-of select="price"/>        

            </price>
            <stock>
            
                <xsl:value-of select="stock"/>        

            </stock>
            <image>
            
                <xsl:value-of select="image"/>        

            </image>
        </product>

    </xsl:for-each>

</products>
</xsl:template>

</xsl:stylesheet>
#!/usr/bin/env python3
"""Build all subpages for the thinking-peak website"""

import os

def make_page(title, page_title, content, filename):
    """Generate a complete HTML page with the standard layout"""
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>{title}</title>
<meta name="keywords" content="patent broker, patent brokers, patent brokerage, patent valuation, ip consulting">
<meta name="description" content="{title}">
<link href="menu1.1.css" rel="stylesheet" type="text/css">
<style type="text/css">
body {{
	background-image:url(images/bg.png);
	background-repeat:repeat-x;
	background-position:left top;
	font-size:12px;
	margin: 14px 0;
	padding:0;
	color: #000;
	font-family: Verdana, Geneva, sans-serif;
}}
.bottom-body {{
	margin:0 auto;
	width:1080px;
	background-repeat:no-repeat;
}}
.bottom-body-bg{{
	margin:0 auto;
	background-repeat:repeat-x;
	background-position:left bottom;
}}
#container {{
	margin:0 auto;
	padding:0;
}}
a:link, a:visited {{
	color:#039;
	text-decoration:none;
}}
a:hover, a:active {{
	color:#036;
	text-decoration:none;
}}
h1, h1 a:link, h1 a:visited {{
	font-family:Georgia, "Times New Roman", Times, serif;
	font-size:125%;
	font-weight:bold;
	color:#C00;
	text-decoration:none;
	margin:5px 8px;
}}
h1 a:hover, h1 a:active {{
	color:#900;
}}
p {{
	font-size:90%;
	margin:5px 15px;
}}
ul li {{
	list-style:none;
	list-style-type:none;
}}
form {{
	font-size: 90%;
	margin: 5px 15px;
}}
strong {{
	font-size:110%;
	color:#036;
}}
img {{
	border:0;
}}
#header {{
	text-align:right;
	margin-bottom:15px;
}}
#menu {{
	float:left;
	margin:-11px auto;
	font-size:90%;
	font-weight:bold;
	width:165px;
}}
#menu a:hover {{
	background-color:#666;
	background-position:left 100%;
	color:#fff;
}}
#main-content {{
	float:left;
	width:895px;
	padding:0 10px;
}}
.left-column {{
	float:left;
	width:584px;
}}
.right-column {{
	float:left;
	width:300px;
	margin-left:10px;
}}
#footer {{
	margin:0 auto;
	height:200px;
}}
.clearfloat {{
	clear:both;
	height:0;
	font-size: 1px;
	line-height: 0px;
}}
.footer-nav {{
	text-align: center;
	font-size: 11px;
	padding: 5px 0;
}}
.footer-nav a {{
	color: #039;
}}
</style>
</head>
<body>
<div class="bottom-body-bg">
<div class="bottom-body">
<div id="container">
	<div id="header">
		<a href="index.html"><img src="images/logo.png" border="0" alt="IPOfferings"></a>
	</div>

    <div id="menu" style="position: relative">
<ul>
	<li><a href="index.html">Home Page</a></li>
	<li><a href="#">Patent Brokerage &raquo;</a>
		<ul>
			<li><a href="patent-brokerage.html">Patent Brokerage and Patent Brokers</a></li>
			<li><a href="patent-marketing.html">Patent Marketing</a></li>
			<li><a href="patent-brokerage-sales.html">Patent Brokerage - Sales</a></li>
			<li><a href="sell-patents.html">Sell Patents</a></li>
			<li><a href="patent-auction.html">The Best Way to Sell a Patent?</a></li>
		</ul>
	</li>
	<li><a href="patents-for-sale.html">Patents for Sale</a></li>
	<li><a href="patent-infringement.html">Patent Infringement</a></li>
	<li><a href="patent-enforcement.html">Patent Enforcement</a></li>
	<li><a href="inventor-advice.html">Inventor Advice</a></li>
	<li><a href="#">IP Acquisition &raquo;</a>
		<ul>
			<li><a href="patent-acquisition.html">Patent Acquisition</a></li>
			<li><a href="buy-patents.html">Buy Patents</a></li>
		</ul>
	</li>
	<li><a href="#">Patent Value &raquo;</a>
		<ul>
			<li><a href="patent-valuation-services.html">Patent Valuation Services</a></li>
			<li><a href="increasing-patent-value.html">Increasing Patent Value</a></li>
		</ul>
	</li>
	<li><a href="#">Patent Licensing &raquo;</a>
		<ul>
			<li><a href="license-patents.html">License Patents</a></li>
			<li><a href="tech-transfer.html">Technology Transfer</a></li>
			<li><a href="patent-licensing-enforcement.html">Licensing and Enforcement</a></li>
		</ul>
	</li>
	<li><a href="#">IP Services &raquo;</a>
		<ul>
			<li><a href="ip-consulting.html">IP Consulting</a></li>
			<li><a href="ip-ma.html">IP M&amp;A</a></li>
		</ul>
	</li>
	<li><a href="patent-leather.html">Patent Leather</a></li>
	<li><a href="glossary.html">Glossary</a></li>
	<li><a href="#">About IPOfferings &raquo;</a>
		<ul>
			<li><a href="in-the-news.html">In the News</a></li>
			<li><a href="faq.html">FAQ</a></li>
			<li><a href="contact.html">Contacting Us</a></li>
			<li><a href="leadership.html">Leadership Team</a></li>
		</ul>
	</li>
</ul>
<div style="margin-top: 20px;">
	<img src="drawings/IndustryTechOutlookCertificate.jpg" width="162" style="padding-bottom: 10px;" align="right" class="leftpadding"><br><br><br><br>
	<img src="drawings/NewWorldReportAward.png" width="162" style="padding-bottom: 10px;" align="right" class="leftpadding"><br><br><br><br>
	<img src="drawings/IPOfferingsAward.jpg" width="162" align="right" class="leftpadding">
</div>
    </div>

    <div id="main-content">
        <h1>{page_title}</h1>
        {content}
        <br class="clearfloat">
    </div>

    <br class="clearfloat">

    <div class="footer-nav">
      <p align="center"><a href="index.html">Home Page</a> &bull; <a href="patent-brokerage.html">Patent Brokerage</a> &bull; <a href="patents-for-sale.html">Patents for Sale</a> &bull; <a href="patent-infringement.html">Patent Infringement</a> &bull; <a href="patent-enforcement.html">Patent Enforcement</a> &bull; <a href="patent-acquisition.html">IP Acquisition</a><br><a href="patent-valuation-services.html">Patent Value</a> &bull; <a href="license-patents.html">Patent Licensing</a> &bull; <a href="ip-consulting.html">IP Services</a> &bull; <a href="patent-leather.html">Patent Leather</a> &bull; <a href="in-the-news.html">About IPOfferings</a> &bull; <a href="resources.html">Resources</a></p>
    </div>

    <div id="footer">
      <p align="center"><a href="sitemap.html"><font color="#808080" size="2">Sitemap</font></a></p>
      <p align="center" style="color:#fff"><font size="1px"><a href="#" style="color:#fff">Ruben Andino</a> - <a href="#" style="color:#fff">Mirian Andino</a> - <a href="#" style="color:#fff">El Faro Apostolico de Brooklyn</a></font></p>
      <img src="images/blue-key.jpg" width="1080" height="154" border="0" alt="">
    </div>

</div>
</div>
</div>
</body>
</html>"""
    
    with open(f'/home/ubuntu/thinking-peak/{filename}', 'w') as f:
        f.write(html)
    print(f"Created {filename}")


# Patent Brokerage page
make_page(
    "Patent Brokerage | Patent Broker | IPOfferings - Patent Brokerage",
    "Patent Brokerage and Patent Brokers",
    """
    <p>Patent brokerage is the selling, licensing or other monetization of a patent by an agent who represents the patent owner. Patent brokerage is a complex process that requires identifying specific applications for the invention covered by a patent, then matching those applications with prospects who are most likely to acquire or license that patent.</p>
    
    <p>Most patent brokers use the same patent brokerage business model. They make cold calls. They agree to represent your patent or portfolio, they develop a list of likely buyers or licensees, and they contact those prospects one by one. By telephone, by email, by regular mail, even via fax. And they keep making cold calls until they receive an offer or they run out of prospects.</p>
    
    <p>IPOfferings is the ONLY patent broker to operate on a totally different and unique patent brokerage business model. ONLY IPOfferings develops, designs and implements a comprehensive marketing campaign for each patent or portfolio we represent. The other patent brokers may claim that they put together a "marketing program" or a "marketing plan" for the patents they represent, but they really just make sales calls. There is no genuine marketing involved in the process. Cold calling is the extent of the patent brokerage services that all the other brokers offer.</p>
    
    <p><strong>&#10022; Comprehensive Marketing Campaign:</strong> IPOfferings is the ONLY patent brokerage firm to actually use proven marketing concepts to promote and sell the patents and portfolios we represent. <strong><em>ONLY IPOfferings implements a marketing campaign that puts our clients' patents in front of tens of thousands of prospects!</em></strong> There are five key elements to the marketing campaigns we develop, design and execute for our clients.</p>
    
    <ul>
    <li><strong>Patent Value Quotient&trade; Report:</strong> IPOfferings is the ONLY patent broker that researches and reports actual patent transactions on an annual basis, and provides that data free-of-charge to the IP and business communities. The data in the <strong>Patent Value Quotient</strong> is used throughout corporate America to establish patent value. This report, first published in 2012, gives IPOfferings a status and reputation that no other patent broker has. Just one of the benefits of being publisher of the <strong>Patent Value Quotient</strong> is that patent buyers come to us. When we agree to represent a patent or portfolio, we sometimes already have buyers lined up to buy it!</li>
    
    <li><strong>IP MarketPlace&trade; Newsletter:</strong> IPOfferings is the ONLY patent brokerage firm that publishes a monthly e-letter that features the patents and portfolios we represent. Some other patent brokers publish newsletters, but they do not feature the patents they represent in their newsletters. <strong>IP MarketPlace</strong> goes to over 9,000 opt-in corporate and IP executives. In the time it would take to cold call one prospect, IPOfferings reaches thousands of prospects! When a property is featured in <strong>IP MarketPlace</strong>, we often receive inquiries that turn into prospects that turn into buyers or licensees &ndash; without ever making any cold calls!</li>
    
    <li><strong>Patent Marketplace:</strong> IPOfferings is the ONLY patent broker to list the patents and portfolios it represents at a search-engine-optimized (SEO) website. Some patent brokerage firms list the properties they represent at their websites, but no one ever visits those websites, so no one ever sees them! Go to any search engine and type in "patent broker" or "patent brokerage" or "patents for sale" and see what patent broker websites show up on the first page of search results. The sites that rank in the Top 10 &ndash; like www.IPOfferings.com &ndash; get thousands of visitors. The website that ranks 11th or 111th or 1,011th gets NO visitors! The IPOfferings site appears right at the top of the search results, and that insures that the patents and portfolios we list in the <strong>Patent MarketPlace</strong> section of our website will be seen by those looking to acquire or license patents.</li>
    
    <li><strong>Trade Press Coverage:</strong> IPOfferings is the ONLY patent brokerage firm to generate news coverage for the patents and portfolios we represent in the trade press for that property's industry. At the <a href="in-the-news.html">In the News</a> page at our website you will see just some of the most recent news coverage we've generated for the patents and portfolios we represent. A typical trade magazine will go to tens of thousands of industry executives, and will expose the patents and portfolios represented by IPOfferings to buyers or licensees that no broker would have ever located via cold calling.</li>
    
    <li><strong>Superior Marketing Piece:</strong> IPOfferings is the ONLY patent brokerage firm to produce a state-of-the-art marketing piece for each patent or property we represent that can be read on three different levels. The typical marketing piece developed by the typical patent broker looks like a college term paper &ndash; page after page of paragraphs of text &ndash; and they are deathly dull. Request an IPOfferings' Patent Brokerage Prospectus, then ask another broker for a sample of what it sends out to prospects, compare the two, and you be the judge. Whom do you want to develop and design a marketing piece for your patent(s)?</li>
    </ul>
    
    <p>Once we've executed our unique marketing campaign for a client we've often received numerous inquiries, a handful of serious prospects, and a few offers. And we are able to close a deal and monetize our client's patent(s) without ever making a single out-bound sales call.</p>
    
    <p><strong>&#10022; Comprehensive Sales Campaign:</strong> However, if our marketing program does not generate sufficient offers, we then turn to what every other patent broker does. We generate a prospect list, and take the patent or portfolio to prospective buyers or licensees. Our years of experience have taught us who the key decision makers are at a business when it comes to acquiring a patent. In many cases, we already know this person. If we do not, we have proprietary technology that enables us to quickly identify and reach exactly the right people. And, because of our excellent reputation and high profile in the IP community, we are able to get the properties we represent in front of buyers and licensees that other patent brokers never get to talk to!</p>
    
    <p>By spreading the widest possible net using proven marketing techniques, IPOfferings is able to put our clients' patents in front of thousand more prospects than any other patent brokers could ever reach by just making cold calls. In fact, we often receive inquiries that develop into prospects that develop into buyers or licensees from companies we did not know existed, and no broker would have ever cold called!</p>
    
    <p>You will have one chance to sell or license your patent or patent portfolio. The patent broker you select will definitely make a difference.</p>
    
    <p>For most clients, IPOfferings works on a Partial Contingency basis. The client pays a modest one-time up-front fee to cover the Marketing Program, and IPOfferings then implements a comprehensive Sales Campaign on a contingency basis, taking a sliding Success Fee from the revenue we generate from the sale, licensing, or other monetization of our client's patent or patents.</p>
    
    <p>If we do not believe that we can successfully monetize a patent or portfolio, we will let the patentee know that we have decided to decline to take on the patent or portfolio as a brokerage project. If requested, we will refer the patentee to other firms that may be help to assist.</p>
    
    <p>The next step is to contact us at <a href="mailto:info@ipofferings.com">info@IPOfferings.com</a> or 845-337-6911. Be sure to download our <a href="#">Patent Brokerage Services</a> data sheet.</p>
    """,
    "patent-brokerage.html"
)

# Patents for Sale page
make_page(
    "Patents for Sale | Patent Marketplace | IPOfferings",
    "Patents for Sale",
    """
    <p>IPOfferings represents patents and patent portfolios for sale or license in a wide range of technology areas. We are the ONLY patent broker to develop and execute a comprehensive marketing campaign for each patent or portfolio we represent. Our <strong>Patent MarketPlace</strong> features the latest patents available for sale or license.</p>
    
    <p>If you are looking to <a href="buy-patents.html">buy patents</a> or acquire a patent portfolio, you've come to the right place. IPOfferings represents a wide range of patents in many technology areas. Contact us at <a href="mailto:patents@ipofferings.com">patents@ipofferings.com</a> or 845-337-6911 to discuss your patent acquisition needs.</p>
    
    <p>If you have patents you would like to sell or license, please review our <a href="patent-brokerage.html">Patent Brokerage</a> services and contact us to discuss how we can help you monetize your intellectual property assets.</p>
    
    <p>To be notified of new patents as they come to market, sign up for our free monthly <strong>IP MarketPlace&trade;</strong> newsletter at the <a href="index.html">Home Page</a>.</p>
    """,
    "patents-for-sale.html"
)

# Patent Infringement page
make_page(
    "Patent Infringement | Claim Charts | IPOfferings",
    "Patent Infringement and Claim Charts",
    """
    <p>If you believe that your patent has been infringed, that is serious business. But the burden of proof of patent infringement lies with the patent owner. That is why IPOfferings offers two services: Patent Infringement Analysis and Claim Chart development.</p>
    
    <p>We can help you identify and document with Claim Charts the infringers of your patent so you can pursue the infringers and secure compensation for infringement of your patent or patents!</p>
    
    <h1>Patent Infringement Analysis</h1>
    <p>IPOfferings will analyze your patent and identify potential infringers. We will review the claims of your patent and compare them to products and processes in the marketplace to identify potential infringers. Our Patent Infringement Analysis will give you the information you need to decide whether to pursue infringers.</p>
    
    <h1>Claim Chart Development</h1>
    <p>A Claim Chart is a document that maps the claims of a patent to specific products or processes that are alleged to infringe those claims. Claim Charts are essential for patent enforcement and litigation. IPOfferings will develop professional Claim Charts that document infringement of your patent in a clear and compelling manner.</p>
    
    <p>To learn more about our Patent Infringement Analysis and Claim Chart services, contact IPOfferings at <a href="mailto:patents@ipofferings.com">patents@ipofferings.com</a> or 845-337-6911.</p>
    """,
    "patent-infringement.html"
)

# Patent Enforcement page
make_page(
    "Patent Enforcement | IPOfferings",
    "Patent Enforcement",
    """
    <p>If you believe your patent has been infringed, and you can document that infringement, IPOfferings can assist you in finding a strategic partner that can assert your patents against any and all infringers, and do so on a contingency basis, both managing and financing a comprehensive patent enforcement campaign, and sharing the proceeds of any settlements, licenses or awards with you.</p>
    
    <p>Patent enforcement is a complex and expensive process. IPOfferings works with a network of experienced patent litigation firms and patent assertion entities (PAEs) that specialize in patent enforcement. We can help you find the right partner to enforce your patents and maximize the return on your intellectual property investment.</p>
    
    <p>To learn more about our Patent Enforcement services, contact IPOfferings at <a href="mailto:patents@ipofferings.com">patents@ipofferings.com</a> or 845-337-6911.</p>
    """,
    "patent-enforcement.html"
)

# Inventor Advice page
make_page(
    "Inventor Advice | First Time Inventors | IPOfferings",
    "Inventor Advice",
    """
    <p>If you are a first-time inventor, you have many questions. IPOfferings has been working with inventors for many years, and we have compiled some advice for first-time inventors.</p>
    
    <h1>Get a Patent</h1>
    <p>Before you can sell or license your invention, you need to protect it with a patent. A patent gives you the exclusive right to make, use, and sell your invention for a period of 20 years from the date of filing. Without a patent, anyone can copy your invention and you have no legal recourse.</p>
    
    <h1>Understand Your Patent</h1>
    <p>Once you have a patent, you need to understand what it covers. The claims of your patent define the scope of your patent protection. You should work with your patent attorney to understand the claims of your patent and what they cover.</p>
    
    <h1>Assess the Value of Your Patent</h1>
    <p>Not all patents are created equal. Some patents cover inventions that have significant commercial value, while others cover inventions that have little or no commercial value. IPOfferings offers <a href="patent-valuation-services.html">Patent Valuation Services</a> to help you assess the value of your patent.</p>
    
    <h1>Contact IPOfferings</h1>
    <p>If you have a patent that you believe has commercial value, contact IPOfferings at <a href="mailto:patents@ipofferings.com">patents@ipofferings.com</a> or 845-337-6911. We will review your patent and let you know if it is a good candidate for our patent brokerage services.</p>
    """,
    "inventor-advice.html"
)

# Patent Acquisition page
make_page(
    "Patent Acquisition | Buy Patents | IPOfferings",
    "Patent Acquisition",
    """
    <p>IPOfferings helps businesses, universities, and other organizations acquire patents and patent portfolios that are aligned with their technology and business strategies. Whether you are looking to build a defensive patent portfolio, acquire patents for licensing, or purchase patents to block competitors, IPOfferings can help.</p>
    
    <p>Our patent acquisition services include:</p>
    <ul>
    <li><strong>Patent Search:</strong> We will search for patents that are available for sale or license that match your technology and business needs.</li>
    <li><strong>Patent Evaluation:</strong> We will evaluate the patents we find to determine their quality, scope, and commercial value.</li>
    <li><strong>Patent Negotiation:</strong> We will negotiate the acquisition of patents on your behalf, working to secure the best possible terms.</li>
    <li><strong>Patent Due Diligence:</strong> We will conduct due diligence on patents you are considering acquiring to identify any potential issues.</li>
    </ul>
    
    <p>To learn more about our Patent Acquisition services, contact IPOfferings at <a href="mailto:patents@ipofferings.com">patents@ipofferings.com</a> or 845-337-6911.</p>
    """,
    "patent-acquisition.html"
)

# Buy Patents page
make_page(
    "Buy Patents | Patent Acquisition | IPOfferings",
    "Buy Patents",
    """
    <p>If you are looking to buy patents, IPOfferings can help. We represent a wide range of patents and patent portfolios that are available for sale or license. Our <strong>Patent MarketPlace</strong> features the latest patents available for acquisition.</p>
    
    <p>IPOfferings also offers a patent search service. If you are looking for patents in a specific technology area, we can search for patents that are available for sale or license that match your needs.</p>
    
    <p>To learn more about buying patents through IPOfferings, contact us at <a href="mailto:patents@ipofferings.com">patents@ipofferings.com</a> or 845-337-6911.</p>
    """,
    "buy-patents.html"
)

# Patent Valuation Services page
make_page(
    "Patent Valuation Services | Patent Value | IPOfferings",
    "Patent Valuation Services",
    """
    <p>As the premier patent brokerage and IP consulting services firm in the U.S., no organization knows more about patent value than IPOfferings. We offer not just one, but three, Patent Valuation Services.</p>
    
    <h1>Patent Value Quotient&trade; (PVQ)</h1>
    <p>The <strong>Patent Value Quotient</strong> is IPOfferings' proprietary patent valuation tool. The PVQ is based on actual patent transaction data that IPOfferings has collected over many years of brokering patent transactions. The PVQ provides a quick, cost-effective way to get a ballpark estimate of the value of your patent.</p>
    
    <h1>Patent Valuation Report</h1>
    <p>For a more detailed patent valuation, IPOfferings offers a comprehensive Patent Valuation Report. This report provides a thorough analysis of the value of your patent, including an analysis of the patent's claims, the technology covered by the patent, the market for the technology, and comparable patent transactions.</p>
    
    <h1>Expert Witness Valuation</h1>
    <p>If you need a patent valuation for litigation or other legal purposes, IPOfferings can provide an expert witness valuation. Our expert witness valuations are prepared by experienced patent valuation experts who can testify in court about the value of your patent.</p>
    
    <p>To learn more about our Patent Valuation Services, contact IPOfferings at <a href="mailto:patents@ipofferings.com">patents@ipofferings.com</a> or 845-337-6911.</p>
    """,
    "patent-valuation-services.html"
)

# Increasing Patent Value page
make_page(
    "Increasing Patent Value | IPOfferings",
    "Increasing Patent Value",
    """
    <p>There are several things you can do to increase the value of your patent before you sell or license it. IPOfferings can help you identify and implement strategies to maximize the value of your patent.</p>
    
    <h1>Broaden Your Claims</h1>
    <p>The claims of your patent define the scope of your patent protection. Broader claims generally mean greater patent value. If your patent has narrow claims, you may be able to file continuation applications with broader claims to increase the scope of your patent protection.</p>
    
    <h1>Build a Patent Portfolio</h1>
    <p>A portfolio of related patents is generally more valuable than a single patent. If you have multiple patents in the same technology area, you may be able to bundle them into a portfolio and sell or license the portfolio as a whole.</p>
    
    <h1>Document Infringement</h1>
    <p>If your patent is being infringed, documenting that infringement can significantly increase the value of your patent. Potential buyers or licensees will pay more for a patent that has documented infringement because it gives them a clear path to revenue.</p>
    
    <p>To learn more about how to increase the value of your patent, contact IPOfferings at <a href="mailto:patents@ipofferings.com">patents@ipofferings.com</a> or 845-337-6911.</p>
    """,
    "increasing-patent-value.html"
)

# License Patents page
make_page(
    "License Patents | Patent Licensing | IPOfferings",
    "License Patents",
    """
    <p>Patent licensing is the process of granting permission to another party to use your patented invention in exchange for royalties or other compensation. Patent licensing can be a very effective way to monetize your patent without selling it.</p>
    
    <p>IPOfferings offers comprehensive patent licensing services. We will identify potential licensees for your patent, negotiate licensing agreements on your behalf, and help you maximize the royalties you receive from your patent.</p>
    
    <p>Our patent licensing services include:</p>
    <ul>
    <li><strong>Licensee Identification:</strong> We will identify companies that are using or could use the technology covered by your patent.</li>
    <li><strong>Licensing Negotiation:</strong> We will negotiate licensing agreements on your behalf, working to secure the best possible royalty rates and terms.</li>
    <li><strong>Licensing Program Management:</strong> We will manage your patent licensing program, tracking royalty payments and ensuring compliance with licensing agreements.</li>
    </ul>
    
    <p>To learn more about our Patent Licensing services, contact IPOfferings at <a href="mailto:patents@ipofferings.com">patents@ipofferings.com</a> or 845-337-6911.</p>
    """,
    "license-patents.html"
)

# IP Consulting page
make_page(
    "IP Consulting | Intellectual Property Consulting | IPOfferings",
    "IP Consulting",
    """
    <p>We help owners of Intellectual Property better utilize their IP assets. This includes putting a fair market value on patent, copyrights, trademarks and other IP, performing an independent analysis your patent portfolio, and assisting in the execution of an IP strategy and an IP lifecycle system. We also provide due diligence for M&amp;A firms, investment bankers, venture capitalists, hedge funds and other financial institutions.</p>
    
    <h1>IP Strategy</h1>
    <p>IPOfferings can help you develop an IP strategy that aligns with your business goals. We will analyze your current IP portfolio, identify gaps and opportunities, and help you develop a plan to build and leverage your IP assets.</p>
    
    <h1>IP Portfolio Analysis</h1>
    <p>IPOfferings can perform an independent analysis of your patent portfolio to identify your strongest patents, your weakest patents, and opportunities to strengthen your portfolio. Our portfolio analysis will help you make informed decisions about which patents to maintain, which to sell or license, and which to let expire.</p>
    
    <h1>IP Due Diligence</h1>
    <p>If you are considering acquiring a company or investing in a company, IPOfferings can perform IP due diligence to assess the quality and value of the company's IP assets. Our IP due diligence services are used by M&amp;A firms, investment bankers, venture capitalists, hedge funds, and other financial institutions.</p>
    
    <p>To learn more about our IP Consulting services, contact IPOfferings at <a href="mailto:patents@ipofferings.com">patents@ipofferings.com</a> or 845-337-6911.</p>
    """,
    "ip-consulting.html"
)

# Patent Leather page
make_page(
    "Patent Leather | IP News and Views | IPOfferings",
    "Patent Leather",
    """
    <p><strong>Patent Leather</strong> is IPOfferings' popular &ndash; sometimes funny, sometimes serious, but always pretentious &ndash; commentary on the world of patents and intellectual property. Patent Leather appears in each issue of our monthly <strong>IP MarketPlace&trade;</strong> newsletter.</p>
    
    <p>To receive <strong>Patent Leather</strong> and all the other great content in <strong>IP MarketPlace</strong>, sign up for our free newsletter at the <a href="index.html">Home Page</a>.</p>
    """,
    "patent-leather.html"
)

# Glossary page
make_page(
    "Patent Glossary | IP Glossary | IPOfferings",
    "Patent and IP Glossary",
    """
    <p>The following is a glossary of common terms used in the patent and intellectual property fields.</p>
    
    <p><strong>Assignment:</strong> The transfer of ownership of a patent from one party to another.</p>
    
    <p><strong>Claim:</strong> A statement in a patent that defines the scope of the patent protection. Claims are the most important part of a patent.</p>
    
    <p><strong>Continuation Application:</strong> A patent application that claims priority to an earlier patent application and adds new claims.</p>
    
    <p><strong>Copyright:</strong> A form of intellectual property protection that protects original works of authorship, such as books, music, and software.</p>
    
    <p><strong>Infringement:</strong> The unauthorized use of a patented invention.</p>
    
    <p><strong>Intellectual Property (IP):</strong> A broad term that refers to patents, trademarks, copyrights, trade secrets, and other forms of intangible property.</p>
    
    <p><strong>License:</strong> Permission granted by a patent owner to another party to use the patented invention in exchange for royalties or other compensation.</p>
    
    <p><strong>Patent:</strong> A government-granted right that gives the patent owner the exclusive right to make, use, and sell an invention for a period of 20 years from the date of filing.</p>
    
    <p><strong>Patent Broker:</strong> An agent who represents patent owners in the sale, licensing, or other monetization of their patents.</p>
    
    <p><strong>Patent Portfolio:</strong> A collection of patents owned by a single entity.</p>
    
    <p><strong>Prior Art:</strong> Any evidence that an invention was known or used before the filing date of a patent application.</p>
    
    <p><strong>Royalty:</strong> A payment made by a licensee to a patent owner in exchange for the right to use the patented invention.</p>
    
    <p><strong>Trade Secret:</strong> Confidential business information that provides a competitive advantage.</p>
    
    <p><strong>Trademark:</strong> A word, phrase, symbol, or design that identifies and distinguishes the source of goods or services.</p>
    """,
    "glossary.html"
)

# Contact page
make_page(
    "Contact IPOfferings | Patent Broker | IP Consulting",
    "Contacting Us",
    """
    <p>IPOfferings LLC<br>
    75 Montebello Road<br>
    Suffern, NY 10901</p>
    
    <p>Phone: 845-337-6911<br>
    Email: <a href="mailto:patents@ipofferings.com">patents@ipofferings.com</a></p>
    
    <p>Whether you want to sell, license, or acquire patents, or you need IP consulting services, IPOfferings is here to help. Contact us today to discuss how we can help you optimize the value of your intellectual property.</p>
    """,
    "contact.html"
)

# In the News page
make_page(
    "In the News | IPOfferings Press Coverage",
    "In the News",
    """
    <p>IPOfferings generates news coverage for the patents and portfolios we represent in the trade press for each property's industry. Below are some of the most recent news articles featuring IPOfferings and the patents and portfolios we represent.</p>
    
    <p>For more information about IPOfferings and our patent brokerage and IP consulting services, contact us at <a href="mailto:patents@ipofferings.com">patents@ipofferings.com</a> or 845-337-6911.</p>
    """,
    "in-the-news.html"
)

# FAQ page
make_page(
    "FAQ | Frequently Asked Questions | IPOfferings",
    "Frequently Asked Questions",
    """
    <p><strong>Q: What is a patent broker?</strong><br>
    A: A patent broker represents patent owners in the sale, licensing, or other monetization of their patents. A patent broker matches the technology covered by a patent with prospective buyers or licensees who have a need for that technology.</p>
    
    <p><strong>Q: How does IPOfferings differ from other patent brokers?</strong><br>
    A: IPOfferings is the ONLY patent broker to develop and execute a comprehensive marketing campaign for each patent or portfolio we represent. Other patent brokers simply make cold calls. IPOfferings uses proven marketing techniques to put our clients' patents in front of tens of thousands of prospects.</p>
    
    <p><strong>Q: How much does it cost to use IPOfferings' patent brokerage services?</strong><br>
    A: For most clients, IPOfferings works on a Partial Contingency basis. The client pays a modest one-time up-front fee to cover the Marketing Program, and IPOfferings then implements a comprehensive Sales Campaign on a contingency basis, taking a sliding Success Fee from the revenue we generate.</p>
    
    <p><strong>Q: What types of patents does IPOfferings represent?</strong><br>
    A: IPOfferings represents patents in a wide range of technology areas, including software, electronics, mechanical devices, medical devices, consumer products, and more.</p>
    
    <p><strong>Q: How do I get started with IPOfferings?</strong><br>
    A: Contact us at <a href="mailto:patents@ipofferings.com">patents@ipofferings.com</a> or 845-337-6911. We will review your patent and let you know if it is a good candidate for our patent brokerage services.</p>
    """,
    "faq.html"
)

# Resources page
make_page(
    "Resources | Patent Resources | IPOfferings",
    "Resources",
    """
    <p>IPOfferings provides a number of resources to help patent owners, buyers, and licensees navigate the complex world of patents and intellectual property.</p>
    
    <p><strong>IP MarketPlace&trade; Newsletter:</strong> Our free monthly newsletter features the latest patents available for sale or license, along with IP-related news and views. Sign up at the <a href="index.html">Home Page</a>.</p>
    
    <p><strong>Patent Value Quotient&trade;:</strong> Our annual report on patent transaction data, used throughout corporate America to establish patent value.</p>
    
    <p><strong>Patent Leather:</strong> Our popular commentary on the world of patents and intellectual property. Read the latest <a href="patent-leather.html">Patent Leather</a>.</p>
    
    <p><strong>Glossary:</strong> A glossary of common terms used in the patent and intellectual property fields. See our <a href="glossary.html">Patent and IP Glossary</a>.</p>
    """,
    "resources.html"
)

# Sitemap page
make_page(
    "Sitemap | IPOfferings",
    "Sitemap",
    """
    <p><a href="index.html">Home Page</a></p>
    <p><strong>Patent Brokerage</strong></p>
    <ul>
    <li><a href="patent-brokerage.html">Patent Brokerage and Patent Brokers</a></li>
    <li><a href="patent-marketing.html">Patent Marketing</a></li>
    <li><a href="patent-brokerage-sales.html">Patent Brokerage - Sales</a></li>
    <li><a href="sell-patents.html">Sell Patents</a></li>
    <li><a href="patent-auction.html">The Best Way to Sell a Patent?</a></li>
    </ul>
    <p><a href="patents-for-sale.html">Patents for Sale</a></p>
    <p><a href="patent-infringement.html">Patent Infringement</a></p>
    <p><a href="patent-enforcement.html">Patent Enforcement</a></p>
    <p><a href="inventor-advice.html">Inventor Advice</a></p>
    <p><strong>IP Acquisition</strong></p>
    <ul>
    <li><a href="patent-acquisition.html">Patent Acquisition</a></li>
    <li><a href="buy-patents.html">Buy Patents</a></li>
    </ul>
    <p><strong>Patent Value</strong></p>
    <ul>
    <li><a href="patent-valuation-services.html">Patent Valuation Services</a></li>
    <li><a href="increasing-patent-value.html">Increasing Patent Value</a></li>
    </ul>
    <p><strong>Patent Licensing</strong></p>
    <ul>
    <li><a href="license-patents.html">License Patents</a></li>
    <li><a href="tech-transfer.html">Technology Transfer</a></li>
    <li><a href="patent-licensing-enforcement.html">Licensing and Enforcement</a></li>
    </ul>
    <p><strong>IP Services</strong></p>
    <ul>
    <li><a href="ip-consulting.html">IP Consulting</a></li>
    <li><a href="ip-ma.html">IP M&amp;A</a></li>
    </ul>
    <p><a href="patent-leather.html">Patent Leather</a></p>
    <p><a href="glossary.html">Glossary</a></p>
    <p><strong>About IPOfferings</strong></p>
    <ul>
    <li><a href="in-the-news.html">In the News</a></li>
    <li><a href="faq.html">FAQ</a></li>
    <li><a href="contact.html">Contacting Us</a></li>
    <li><a href="leadership.html">Leadership Team</a></li>
    </ul>
    <p><a href="resources.html">Resources</a></p>
    """,
    "sitemap.html"
)

# Additional pages
for page_info in [
    ("patent-marketing.html", "Patent Marketing | IPOfferings", "Patent Marketing",
     "<p>IPOfferings develops and executes comprehensive marketing campaigns for each patent or portfolio we represent. Our patent marketing services include newsletter marketing, website marketing, trade press coverage, and direct marketing to prospective buyers and licensees.</p><p>Contact us at <a href='mailto:patents@ipofferings.com'>patents@ipofferings.com</a> or 845-337-6911 to learn more.</p>"),
    ("patent-brokerage-sales.html", "Patent Brokerage Sales | IPOfferings", "Patent Brokerage - Sales",
     "<p>IPOfferings executes a comprehensive sales campaign for each patent or portfolio we represent. Our sales campaign includes identifying and contacting prospective buyers and licensees, presenting our clients' patents in a professional and compelling manner, and negotiating the best possible terms for our clients.</p><p>Contact us at <a href='mailto:patents@ipofferings.com'>patents@ipofferings.com</a> or 845-337-6911 to learn more.</p>"),
    ("sell-patents.html", "Sell Patents | Patent Broker | IPOfferings", "Sell Patents",
     "<p>If you have patents you want to sell, IPOfferings can help. We are the ONLY patent broker to develop and execute a comprehensive marketing campaign for each patent or portfolio we represent. Contact us at <a href='mailto:patents@ipofferings.com'>patents@ipofferings.com</a> or 845-337-6911 to get started.</p>"),
    ("patent-auction.html", "Patent Auction | Best Way to Sell a Patent | IPOfferings", "The Best Way to Sell a Patent?",
     "<p>Is a patent auction the best way to sell a patent? IPOfferings believes that a comprehensive marketing campaign is far more effective than a patent auction for most patents. Contact us at <a href='mailto:patents@ipofferings.com'>patents@ipofferings.com</a> or 845-337-6911 to learn more about our approach.</p>"),
    ("tech-transfer.html", "Technology Transfer | Technology Licensing | IPOfferings", "Technology Transfer",
     "<p>Technology transfer is the process of transferring technology from one organization to another. IPOfferings can help you identify and execute technology transfer opportunities. Contact us at <a href='mailto:patents@ipofferings.com'>patents@ipofferings.com</a> or 845-337-6911 to learn more.</p>"),
    ("patent-licensing-enforcement.html", "Patent Licensing and Enforcement | IPOfferings", "Licensing and Enforcement",
     "<p>IPOfferings provides comprehensive patent licensing and enforcement services. We can help you identify potential licensees, negotiate licensing agreements, and enforce your patents against infringers. Contact us at <a href='mailto:patents@ipofferings.com'>patents@ipofferings.com</a> or 845-337-6911 to learn more.</p>"),
    ("ip-ma.html", "IP M&A | Intellectual Property Mergers and Acquisitions | IPOfferings", "IP M&amp;A",
     "<p>IPOfferings provides IP due diligence services for mergers and acquisitions. We can help you assess the quality and value of a company's IP assets before you acquire it. Contact us at <a href='mailto:patents@ipofferings.com'>patents@ipofferings.com</a> or 845-337-6911 to learn more.</p>"),
    ("leadership.html", "Leadership Team | IPOfferings", "Leadership Team",
     "<p>IPOfferings is led by a team of experienced patent brokers and IP consultants with decades of experience in the patent and intellectual property fields. Contact us at <a href='mailto:patents@ipofferings.com'>patents@ipofferings.com</a> or 845-337-6911 to learn more about our team.</p>"),
]:
    filename, title, page_title, content = page_info
    make_page(title, page_title, content, filename)

print("\nAll pages created successfully!")
